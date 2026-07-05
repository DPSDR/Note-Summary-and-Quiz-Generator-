import streamlit as st
from api_call import note_generator, audio_transciption, quiz_generator
from PIL import Image

st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note Summary and Quiz")
st.divider()

with st.sidebar:
    st.header("Controls")

    #Images
    images = st.file_uploader(
        "Upload the photos of your note",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )
    if images:
        if len(images) > 3:
            st.error("Upload atmost 3 images")
        else:
            col = st.columns(len(images))
            st.subheader("Uploaded images")
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    #Difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of the quiz",
        ["Easy", "Medium", "Hard"],
        index=None
    )
    pressed = st.button("Click the button to initiate AI", type="primary")

if pressed:
    if not images:
        st.error("You must upload 1 images")
    if not selected_option:
        st.error("You must select a difficulty")
    
    if images and selected_option:

        #Notes
        with st.container(border=True):
            st.subheader("Your Note", anchor=False)

            #PIL image convert
            pil_images = []
            for img in images:
                pil_img = Image.open(img)
                pil_images.append(pil_img)

            #Generate Notes by API call
            with st.spinner("AI is writing note for you..."):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)


        #Audio transription
        with st.container(border=True):
            st.subheader("Audio Transcription", anchor=False)

            #Replace by API call
            with st.spinner("AI is preparing audio for you..."):

                #clearing the markdown signs
                generated_notes = generated_notes.replace("#", "")
                generated_notes = generated_notes.replace("*", "")
                generated_notes = generated_notes.replace("_", "")
                generated_notes = generated_notes.replace("`", "")
                generated_notes = generated_notes.replace(">", "")
                generated_notes = generated_notes.replace("|", "")

                audio_transcipt = audio_transciption(generated_notes)
                st.audio(audio_transcipt)

        #Quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option} Level)", anchor=False)

            #Replace by API call
            with st.spinner("Preparing the quizzes..."):
                quizzes = quiz_generator(pil_images, selected_option)
                st.markdown(quizzes)

