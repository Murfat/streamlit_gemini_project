import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

# Title Related Code
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3(Three) images to Generate Note Summary and Quizzes")
st.divider()

#Sidebar
with st.sidebar:
    st.header("Controls")

    #To get images from user
    images = st.file_uploader(
        "Upload the photos of your note",
        type = ["jpg", "jpeg", "png"],
        accept_multiple_files = True
    )

    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)


    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded Images")

            col = st.columns(len(images))

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #Quiz Difficulty Level
    seleted_option = st.selectbox(
        "Enter the Difficulty Level of Quiz",
        ("Easy", "Medium", "Hard"),
        index = None 
    )

    pressed= st.button("Click the button to initiate AI", type="primary")

if pressed:
    if not images:
        st.error("You must upload atleast 1 (One) image")
    if not seleted_option:
        st.error("You must select a difficulty level")

    if images and seleted_option:
        # Note Generation
        with st.container(border=True):
            st.subheader("Your note")

            with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        #Audio Transcript
        with st.container(border=True):
            st.subheader("Audio Transcription")

            with st.spinner("AI is generating audio for you"):

                #Clearing the markdown 
                generated_notes = generated_notes.replace("#", "")
                generated_notes = generated_notes.replace("*", "")
                generated_notes = generated_notes.replace("-", "")
                generated_notes = generated_notes.replace("'", "")

                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)

        #Quiz
        with st.container(border=True):
            st.subheader(f"Quiz {seleted_option} Difficulty")

            with st.spinner("AI is generating the quizzes"):
                quizzes = quiz_generator(pil_images, seleted_option)
                st.markdown(quizzes)
