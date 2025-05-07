import pyttsx3
import datetime
import speech_recognition as sr

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize Text-to-Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        talk("Good Afternoon Sir!")
    else:
        talk("Good Evening Sir!")
    talk("Hello, I am Jarvis. How can I help you?")

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)

    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

# LLM Setup
template = """
Answer the Question Below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3")  
chain = prompt | model
context = ""

def ask_llm(query):
    global context
    response = chain.invoke({"context": context, "question": query})
    context += f"\nUser: {query}\nAI: {response}"
    print("Jarvis:", response)
    talk(response)

# Main Function
if __name__ == "__main__":
    greet()
    while True:
        query = listen().lower()
        if 'exit' in query or 'stop' in query:
            talk("Okay, Sir! As you say.")
            break
        elif query != "none":
            ask_llm(query)
