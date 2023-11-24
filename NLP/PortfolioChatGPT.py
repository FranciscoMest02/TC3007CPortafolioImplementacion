import streamlit as st
import openai
import whisper

openai.api_key = "------"
model = whisper.load_model("base")

st.title("Transcriber and summarizer")
st.subheader("Francisco Mestizo Hernández A01731549")
st.write('\n\n')

file_path = st.text_input("Enter a file name","Write Here...")

def transcribe_audio(model, file_path):
    transcript = model.transcribe(file_path)
    return transcript['text']

def CustomChatGPT(user_input):
    messages = [{"role": "system", "content": "You are an office administer, summarize the text in key points"}]
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    return ChatGPT_reply

if st.button('Transcribe'):
	transcription = transcribe_audio(model, file_path)
	summary = CustomChatGPT(transcription)
	st.write("Summary: \n" + summary)
else:
	st.write("Press the above button..")

