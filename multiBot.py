import gradio as gr
import os
import google.generativeai as genai

# Configure GenAI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the GenerativeModel
model = genai.GenerativeModel("gemini-pro")

# Initialize empty conversation history
conversation_history = []

def generate_response(messages):
    return model.generate_content(messages)

def chatbot(question):
    global conversation_history
    conversation_history.append({'role': 'user', 'parts': [question]})
    response = generate_response(conversation_history)
    conversation_history.append({'role': 'model', 'parts': [response.text]})
    chat_history = "\n".join([f"{msg['role']}: {msg['parts'][0]}" for msg in conversation_history])
    return chat_history

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="Multi Conservation Gemini ChatBot")
iface.launch()
