import tempfile

import openai
from IPython.display import Audio, display
from io import BytesIO


def text_to_speech(message):
    response = openai.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=message
    )
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.write(response.content)
    temp_file.close()

    return temp_file.name


def transcribe_audio(audio):
    if audio is None:
        return "No audio file received."
    try:
        with open(audio, 'rb') as audio_file:
            response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return response.text
    except Exception as e:
        return f"Error during transcription: {e}"

def transcribe_with_whisper(audio):
    # Check if the audio file is passed correctly
    if audio is None:
        return "No audio file received."

    try:
        with open(audio, 'rb') as audio_file:  # Open the audio file to send to the API
            response = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        print( response.text )
        return response.text  # Return the transcription text

    except Exception as e:
        return f"Error during transcription: {e}"
