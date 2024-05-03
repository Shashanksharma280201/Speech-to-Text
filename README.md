# Speech-to-Text

## YouTube Video Transcription and Speech Synthesis

This Python script downloads a YouTube video, extracts its audio, transcribes the audio using the Deepgram API, and then converts the transcription to speech using the Eleven Labs API.

### Requirements
```
- Python 3.x
- pytube : To download YouTube videos.
- moviepy : To extract audio from the video.
- deepgram-sdk : To transcribe the audio using Deepgram API.
- requests : To make HTTP requests for the Eleven Labs API.
```

## Installation

You can install the required libraries using pip:
```
pip install pytube moviepy deepgram-sdk requests
```


## Usage

1. Replace the placeholders for YouTube video URL, Deepgram API key, and Eleven Labs API key with your actual values.
2. Run the script.
3. The script will download the YouTube video, extract its audio, transcribe the audio, and finally synthesize the transcription into speech.

## Important Notes

- Ensure that you have valid API keys for Deepgram and Eleven Labs APIs.
- This script may take some time to run depending on the length of the video and audio transcription.


