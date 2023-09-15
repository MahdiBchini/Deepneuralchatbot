import streamlit as st
import nltk
import speech_recognition as sr

nltk.download('punkt')

def chatbot_response(input_text):
    # Replace this with your chatbot logic
    return "Chatbot Response: You said - " + input_text

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak something...")
        audio = r.listen(source)

    try:
        text_input = r.recognize_google(audio)
        return text_input
    except sr.UnknownValueError:
        return "Sorry, I could not understand your speech."
    except sr.RequestError:
        return "Sorry, there was an error processing your request."

def main():
    st.title("Chatbot with Speech Input")

    # User input choice (Text or Speech)
    input_choice = st.radio("Select Input Type:", ["Text Input", "Speech Input"])

    if input_choice == "Text Input":
        user_input = st.text_input("Enter your text here:")
    else:
        user_input = transcribe_speech()

    if st.button("Submit"):
        if user_input:
            bot_response = chatbot_response(user_input)
            st.write("User Input:", user_input)
            st.write("Chatbot Response:", bot_response)

if __name__ == "__main__":
    main()
