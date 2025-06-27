import gradio as gr
import subprocess
import os
from pydub import AudioSegment
import datetime
import time

# --- Configuration ---
PIPER_EXECUTABLE = "./piper/piper"
VOICES_DIR = "./voices/"
OUTPUT_DIR = "./output/"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Functions ---

def get_available_voices():
    """Loads the list of available voices from the directory."""
    try:
        # Load only files ending with .onnx
        voices = [f for f in os.listdir(VOICES_DIR) if f.endswith(".onnx")]
        # Check if a corresponding .json file exists
        valid_voices = [v for v in voices if os.path.exists(os.path.join(VOICES_DIR, v + ".json"))]
        if not valid_voices:
            gr.Warning("No valid voice pairs (.onnx + .json) were found in the 'voices' directory.")
        return valid_voices
    except FileNotFoundError:
        gr.Warning("The 'voices' directory was not found. Please create it in the main project directory.")
        return []

def synthesize_speech(voice, text, length_scale, noise_scale, save_as_mp3):
    """
    Generates speech from text and returns the path to the audio file for the player 
    and also the path to the file for download.
    """
    if not text or not voice:
        gr.Warning("Please enter text and select a voice.")
        # Return empty updates for both outputs
        return gr.update(value=None), gr.update(value=None)

    # Create a unique filename using a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_filename = f"output_{timestamp}"
    wav_filename = f"{base_filename}.wav"
    output_wav_path = os.path.join(OUTPUT_DIR, wav_filename)

    # Assemble the command for Piper
    command = [
        PIPER_EXECUTABLE,
        "--model", os.path.join(VOICES_DIR, voice),
        "--output_file", output_wav_path,
        "--length_scale", str(length_scale),
        "--noise_scale", str(noise_scale)
    ]

    # Run the Piper process and send the text
    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=text.encode('utf-8'))
        
        if process.returncode != 0:
            # If an error occurs in Piper, display it
            gr.Error(f"Error in Piper: {stderr.decode('utf-8')}")
            return gr.update(value=None), gr.update(value=None)

    except FileNotFoundError:
        gr.Error(f"Error: Piper executable not found at path '{PIPER_EXECUTABLE}'. Please ensure it is correct.")
        return gr.update(value=None), gr.update(value=None)

    # Final path to the file (either WAV or MP3)
    final_output_path = output_wav_path

    # Convert to MP3 if checked
    if save_as_mp3:
        try:
            mp3_filename = f"{base_filename}.mp3"
            final_output_path = os.path.join(OUTPUT_DIR, mp3_filename)
            audio = AudioSegment.from_wav(output_wav_path)
            audio.export(final_output_path, format="mp3")
            os.remove(output_wav_path) # Delete the original WAV file to save space
        except Exception as e:
            gr.Error(f"Error converting to MP3: {e}. Please ensure the ffmpeg system tool is installed.")
            # In case of error, return at least the original WAV
            return gr.update(value=output_wav_path), gr.update(value=output_wav_path) 
    
    # CACHING FIX: Add a unique parameter to force the browser to reload the file.
    unique_path_for_player = f"{final_output_path}?v={time.time()}"
    
    # Return the path for the audio player and the path for the download file
    return unique_path_for_player, final_output_path


# --- Creating the Gradio Interface ---

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# Advanced GUI for Piper TTS")
    
    with gr.Row():
        # Column for main controls
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Text to Synthesize",
                lines=8,
                placeholder="Enter the text you want to be read aloud here..."
            )
            # Load voices and set a default value if any voice exists
            available_voices = get_available_voices()
            default_voice = available_voices[0] if available_voices else None
            voice_dropdown = gr.Dropdown(
                label="Voice",
                choices=available_voices,
                value=default_voice
            )
            synthesize_button = gr.Button("Generate and Play Audio", variant="primary")
        
        # Column for advanced settings
        with gr.Column(scale=1):
            with gr.Accordion("Advanced Voice Settings", open=False):
                length_scale_slider = gr.Slider(
                    minimum=0.5, maximum=2.0, value=1.0, step=0.1,
                    label="Speech Rate (lower = faster)"
                )
                noise_scale_slider = gr.Slider(
                    minimum=0.1, maximum=2.0, value=0.667, step=0.1,
                    label="Voice Variability (higher = more expressive)"
                )
            
            save_as_mp3_checkbox = gr.Checkbox(label="Save as MP3 (smaller file)", value=True)


    gr.Markdown("---")
    # Section for output
    with gr.Row():
        audio_output = gr.Audio(label="Resulting Audio", type="filepath")
        file_download = gr.File(label="Download File", type="filepath")

    # Linking the button to the function
    synthesize_button.click(
        fn=synthesize_speech,
        inputs=[
            voice_dropdown,
            text_input,
            length_scale_slider,
            noise_scale_slider,
            save_as_mp3_checkbox
        ],
        outputs=[audio_output, file_download]
    )

# Launching the application
app.launch()

