# Jarvis - Desktop Voice Assistant 🎙️🧠

This is the **enhanced version** of Jarvis — a Python-powered desktop voice assistant that listens to your voice, understands your query, fetches a smart response using an **LLM (LLaMA 3 via Ollama)**, and speaks it back!

This is the **starter model**, and I plan to **upgrade it into a fully functional personal AI assistant** in the future.

---

## ✨ Features (Current Version)
- Greets the user based on the time of day
- Listens to your voice commands using your microphone
- Uses **Ollama LLaMA 3 model** to answer queries
- Speaks back intelligent responses
- Listens continuously until you say **"exit"** or **"stop"**

---

## 🚀 How to Setup and Run

### 1. Clone the Repository
```bash
git clone https://github.com/KaushallB/Jarvis.git
cd jarvis
```
### 2.Installing Local LLM
1) Visit https://ollama.com/download and download it for your OS (Windows, macOS, Linux). Install and launch it.
2) After installation, open your terminal and run:
  ```bash
ollama pull llama3
```


### 3. Install Required Packages
```bash
pip install pyttsx3 SpeechRecognition pyaudio langchain langchain-ollama ollama
```
### 4.Once everything is set up, launch Jarvis:
```bash
python jarvis.py
```

Speak your queries like:

"Tell me about black holes"

"What is Python?"

"Who is Elon Musk?"

"exit" or "stop" to quit


