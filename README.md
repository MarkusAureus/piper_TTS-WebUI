# Simple Piper TTS Web UI

A lightweight yet powerful Gradio-based web interface for the Piper TTS engine. This application allows you to easily synthesize speech from text using high-quality local voices, with advanced controls for fine-tuning the output. It's designed to be simple, 100% local, and private.

![Application Screenshot](./assets/screenshot.png)


## Features

This application includes several key features to provide a comprehensive text-to-speech experience:

* **Easy to Use Interface:** A clean and intuitive web UI built with Gradio, allowing for easy interaction.
* **Dynamic Voice Selection:** Automatically detects and lists all available Piper voices from your `voices` directory.
* **Advanced Voice Controls:**
    * **Speech Rate:** A slider to control the speed of the generated speech (lower values are faster).
    * **Voice Variability:** A slider to adjust the expressiveness and intonation of the voice (higher values are more expressive).
* **MP3 Export:** An option to save the output directly as a compressed, smaller MP3 file, which is great for sharing or storage.
* **Direct Download:** Easily download the generated audio file (`.wav` or `.mp3`) directly from the interface.
* **100% Local & Private:** The entire process runs on your local machine. No text or audio data is ever sent to the cloud.

## Prerequisites

Before you begin, ensure you have the following installed on your Linux system:

* Python 3.10+
* `pip` and `venv` (usually come with Python)
* `git`
* `ffmpeg` (required for MP3 conversion)

You can install most of these on a Debian-based system (like Ubuntu or Linux Mint) with a single command:
```bash
sudo apt update && sudo apt install git python3-pip python3-venv ffmpeg -y


Setup and Installation
Follow these steps to get the application running. It's crucial to run these commands in the correct order and from the correct directory.
1. Clone the Repository
First, clone this repository to your local machine and navigate into the project directory.
Bash
git clone https://github.com/MarkusAureus/piper_TTS-WebUI
cd YOUR_REPOSITORY_NAME

2. Download Piper Executable
The application needs the Piper engine. Download and unpack it into a piper/ subdirectory inside your project folder.
https://github.com/rhasspy/piper/releases

3. Download Voices
You need to place your voice models (both .onnx and .onnx.json files) into a voices/ subdirectory.
From the main project directory, run these commands:
Bash
# Create the 'voices' directory
mkdir voices

# Download an voice into it
https://github.com/rhasspy/piper/blob/master/VOICES.md

4. Create a Virtual Environment and Install Dependencies
Using a virtual environment is highly recommended to keep dependencies isolated from your system.
Run these commands from the main project directory:
Bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required Python packages
pip install gradio pydub

How to Run the Application
Once the setup is complete, running the application is simple.
    1. Make sure you are in the main project directory and your virtual environment is activated (you should see (venv) at the beginning of your terminal prompt).
    2. Run the main application script:
       Bash
       python3 piper_app.py
       
    3. The application will start and provide a local URL, typically: Running on local URL: http://127.0.0.1:7860
    4. Open this URL in your web browser to start using the GUI.
To stop the application, go back to the terminal and press Ctrl + C.

Directory Structure
For the application to work correctly, your final directory structure should look like this:
YOUR_REPOSITORY_NAME/
├── piper/
│   ├── piper
│   └── ... (other files from the piper archive)
│
├── voices/
│   ├── sk_SK-lili-medium.onnx
│   └── sk_SK-lili-medium.onnx.json
│
├── venv/
│   └── ... (virtual environment files)
│
├── .gitignore   (recommended)
├── piper_app.py
└── README.md

Credits
    • This UI is built using the wonderful Gradio library.
    • The core speech synthesis is powered by the Piper TTS engine.

