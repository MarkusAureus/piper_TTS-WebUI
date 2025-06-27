# Simple Piper TTS Web UI

A lightweight yet powerful Gradio-based web interface for the Piper TTS engine. This application allows you to easily synthesize speech from text using high-quality local voices, with advanced controls for fine-tuning the output. It's designed to be simple, 100% local, and private.

![screenshot]


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



## Piper engine

https://github.com/rhasspy/piper/releases


## More voices

https://github.com/rhasspy/piper/blob/master/VOICES.md
