# Speech-to-Text

# Task 1

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


# Task 2

# Web Scraper for TechCrunch Articles

This is a simple Python script that scrapes the content of a TechCrunch article and prints it out. It utilizes the Beautiful Soup library for parsing HTML content.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Beautiful Soup 4 library

If you're using Google Colab, you can install Beautiful Soup by running the following command in a code cell:
```
!pip install beautifulsoup4 : to run on google colab
pip install beautifulsoup4 : to run on host machine
```
