import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

from deepgram import DeepgramClient, PrerecordedOptions

DEEPGRAM_API_KEY = '3e8e6d68-0225-414d-9c04-c6b6c9f2428b'


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
    
    
# def transcribe_audio(audio_path):
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )
        
        with open(audio_path, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }
        print(audio_path)  # Print the audio path to ensure it's correct
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


# Example usage:
video_url = "https://www.youtube.com/shorts/Fu4AWHjeS_k"
video_path = download_youtube_video(video_url)
if video_path:
    audio_path = extract_audio(video_path)
    # if audio_path:
    #     transcripts = transcribe_audio(audio_path)
    #     if transcripts:
    #         print("Transcripts:")
    #         print(transcripts)
