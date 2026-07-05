from gtts import gTTS
import streamlit as st
import io

text = "Hello, welcome to this course."

speech = gTTS(text, lang="en")
# create an empty buffer
audio_buffer = io.BytesIO()
# write the audio INTO the buffer
speech.write_to_fp(audio_buffer)

st.audio(audio_buffer)