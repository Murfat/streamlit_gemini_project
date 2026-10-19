from google import genai
from dotenv import load_dotenv
import os, io
from gtts import gTTS

# Loading the environment variable
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

# Initializing a client
client = genai.Client(api_key=my_api_key)

# Note Generator
def note_generator(images):
    prompt = """Summarize the picture in note format at max 100 words
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, prompt]
    )

    return response.text

#Audio Transcription
def audio_transcription(text):
    speech = gTTS(text, lang = "en", slow = False)
    audio_buffer = io.BytesIO() 
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(image, diffculty):
    prompt = f"Generate 3 quizzes based on th {diffculty}. Mak sure to add markdown to differentiate the options. Add correct answers at the end of each quizzes"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [image, prompt]
    )

    return response.text