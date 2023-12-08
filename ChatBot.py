import gradio as gr
from gtts import gTTS
from fpdf import FPDF
import re
from bardapi import Bard
import os

os.environ['_BARD_API_KEY']='cQh428X54s5SMvksRnD5NzVI-nfWyDTw_UxnVaqOTvUGIXRE-ciKTzjgsIg7UfHB_1YOMQ.'

class Chatbot:
    def __init__(self):
        self.chat_history = []

    def respond(self, user_input):
      response = Bard().get_answer(user_input)['content']
      self.chat_history.append({"user": user_input, "bot": response})
      translated_speech_path = self.text_to_speech(response)
      chat_history_formatted = "\n".join(f'User: {chat["user"]}\nBot: {chat["bot"]}\n' for chat in self.chat_history)
      return translated_speech_path, response, chat_history_formatted

    def text_to_speech(self, text):
        temp_file = "response.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(temp_file)
        return temp_file

def save_chat_history_as_pdf(chat_history):
    clean_chat_history = re.sub('<br>', '\n', chat_history)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=clean_chat_history)
    pdf_output_path = "chat_history.pdf"
    pdf.output(pdf_output_path)
    return pdf_output_path

def save_chat_history_as_txt(chat_history):
    txt_output_path = "chat_history.txt"
    with open(txt_output_path, "w") as txt_file:
        txt_file.write(chat_history)
    return txt_output_path

def chatbot_response(user_input):
    translated_speech_path, response, chat_history_formatted = chatbot.respond(user_input)
    formatted_chat_history = "\n".join(f'User: {chat["user"]}<br>Bot: {chat["bot"]}<br><br>' for chat in chatbot.chat_history)
    pdf_output_path = save_chat_history_as_pdf(formatted_chat_history)
    return translated_speech_path, response, pdf_output_path, formatted_chat_history

chatbot = Chatbot()

chatbot_interface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs=[
        gr.components.Audio(type='numpy', label="Audio Response"),
        gr.components.Textbox(label="Text Response"),
        gr.components.File(label="Download as PDF"),
        gr.components.HTML(label="Chat History")
    ],
    live=False,
    title="Interactive Chatbot Assistant"
)

chatbot_interface.launch()
