# Project Story

## Inspiration
Growing up in an agricultural background, we encountered challenges accessing veterinary care for cattle. The scarcity of hospitals, the distance to travel, and high doctor charges prompted us to address these pain points. Empathizing with farmers' needs, we envisioned an AI-driven solution.

## What It Does
We developed a Cattle Skin Disease Classifier using a Vision Transformer (LLM model) achieving 100% validation accuracy. Integrated with a Gradio-based AI chatbot doctor, it offers real-time assistance and detailed information about identified diseases, treatments, medicines, and nearby hospitals.

## How We Built It
Data Collection: Faced difficulty in dataset availability, so we created our own using data augmentation techniques.
Algorithm Selection: Transitioned from CNN to LLM models after discovering the effectiveness of Vision Transformers through literature review and research.
AI Chatbot Assistant: Utilized prompting techniques and APIs to provide comprehensive information to users. In AI ChatBot, we implemeted a lot of features like Text-to-speech, current chat, chat history, and download chat.
User Interaction: Implemented Gradio for a user-friendly web interface and hosted on Firebase API.

## Challenges We Ran Into
Dataset Creation: Difficulty in obtaining relevant datasets for cattle skin diseases led us to create our own.
Algorithm Decision: Initial use of CNN yielded lower accuracy, leading us to explore and implement LLM models.
User Interaction: Ensuring a friendly and interactive user experience required refining our web interface and chatbot functionality.

## Accomplishments That We're Proud Of
Achieving 100% validation accuracy with the Vision Transformer model.
Developing an AI chatbot assistant for detailed disease information.
Creating a user-friendly web interface using Gradio.

## What We Learned
Importance of adaptability: Transitioning from CNN to LLM models based on research findings.
Dataset challenges: Overcoming scarcity by employing data augmentation techniques.
User-centric design: Prioritizing user-friendliness and interactivity in the interface.
