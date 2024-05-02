


# Install the Deepgram Python SDK
# pip install deepgram-sdk

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

AUDIO_FILE = "audio_extracted.mp3"


def main():
    try:
        deepgram = DeepgramClient("9a0efccebc0645a6f32582c944466c0dbceff3a9")

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
