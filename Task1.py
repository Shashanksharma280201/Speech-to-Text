# !pip install pytube moviepy deepgram-sdk
# !pip install requests



import os
import requests
from pytube import YouTube
from moviepy.editor import VideoFileClip
from deepgram import DeepgramClient, PrerecordedOptions

# YouTube video URL
video_url = "https://www.youtube.com/shorts/Fu4AWHjeS_k"
# Path for saving downloaded video and extracted audio
output_path = './'

# Deepgram API key
DEEPGRAM_API_KEY = 'DEEPGRAM_API_KEY'
# Eleven Labs API key
ELEVENLABS_API_KEY = "ELEVENLABS_API_KEY"

def download_youtube_video(url, output_path='./'):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        print("Downloading:", yt.title)
        video_path = video.download(output_path)
        print("Download completed!")
        return video_path
    except Exception as e:
        print("Error:", e)
        return None

def extract_audio(video_path, output_path='./'):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio_path = os.path.join(output_path, 'audio_extracted.mp3')
        audio.write_audiofile(audio_path)
        print("Audio extracted successfully!")
        return audio_path
    except Exception as e:
        print("Error:", e)
        return None

def transcribe_audio(audio_path):
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )
        with open(audio_path, "rb") as file:
            buffer_data = file.read()
        payload = {"buffer": buffer_data}
        print(audio_path)  # Print the audio path to ensure it's correct
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        transcript = response.to_dict()["transcripts"][0]["text"]
        return transcript
    except Exception as e:
        print(f"Exception: {e}")
        return None

def text_to_speech(text, voice="en-US", format="mp3"):
    url = "https://api.elevenlabs.io/v1/tts"
    headers = {
        "X-API-Key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice": voice,
        "format": format
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def save_audio(audio_data, filename):
    with open(filename, "wb") as f:
        f.write(audio_data)

def main():
    # Step 1: Download YouTube video
    video_path = download_youtube_video(video_url, output_path)
    if video_path:
        # Step 2: Extract audio from the video
        audio_path = extract_audio(video_path, output_path)
        if audio_path:
            # Step 3: Transcribe audio using Deepgram
            transcript = transcribe_audio(audio_path)
            if transcript:
                # Step 4: Convert transcription to speech
                audio_data = text_to_speech(transcript)
                if audio_data:
                    output_file = "output.mp3"  # Path to save the output audio file
                    save_audio(audio_data, output_file)
                    print(f"Text converted to speech and saved as {output_file}")

if __name__ == "__main__":
    main()
