import requests

def text_to_speech(text, voice="en-US", format="mp3"):
    api_key = "ELEVENLABS_API_KEY"  # Replace with your Eleven Labs API key
    url = "https://api.elevenlabs.io/v1/tts"

    headers = {
        "X-API-Key": api_key,
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
    input_file = "transcription_output.txt"  # Path to your input text file
    output_file = "output.mp3"  # Path to save the output audio file

    try:
        with open(input_file, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    audio_data = text_to_speech(text)
    if audio_data:
        save_audio(audio_data, output_file)
        print(f"Text converted to speech and saved as {output_file}")

if __name__ == "__main__":
    main()
