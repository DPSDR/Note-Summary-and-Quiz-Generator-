from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os, io


#loading the environment variable 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

#initializing a client
client = genai.Client(api_key=api_key)

#note generator
def note_generator(images):
    prompt = "Summarize the picture in note format at max 100 words. Make sure to add necessary markdown to differentiate different section"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text

#audio generator
def audio_transciption(text):
    speech = gTTS(text, lang="en")
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

#quiz difficulty generator
def quiz_generator(image, difficulty):
    prompt = f"Generate 3 quizes based on the {difficulty}. Make sure to add markdown to differentiate the quizzes."

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image, prompt]
    )
    return response.text