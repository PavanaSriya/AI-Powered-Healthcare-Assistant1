import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download('stopwords')

chatbot = pipeline("text-generation",model="distilgpt2")

def hc_cb(user_input):
    if "symptom" in user_input:
        return "Please consult doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the doctor?"
    elif "medicine" in user_input:
        return "Consult doctor for precription according to your health"
    else:
        response=chatbot(user_input,max_length = 500,num_return_sequences=2)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Chatbot")
    user_input = st.text_input("How can i assist you you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ",user_input)
            with st.spinner("Processing..."):
                response=hc_cb(user_input)
            st.write("Healthcare Assistance: ",response)
        else:
            st.write("Please enter a message")

main()
