import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')       

engine.setProperty('voice', voices[0].id)

#print(voices[0].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        talk("Good Morning Sir!")
    elif hour>=12 and hour <18:
        talk('Good Afternoon Sir!')
    else:
        talk('Good Evening Sir!')

    talk('Hello I am Jarvis, How can I help you')


def listen():
    #Taking microphone input from user and return string output
    rec=sr.Recognizer() #To Recognize audio
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold =1
        audio=rec.listen(source)

    try:
        print('Recognizing')
        query=rec.recognize_google(audio,language='en-us')
        print(f"User said :{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please..")
        return "None"
    return query

def search(query):
    talk('Let me call up EDITH to find that for you!')
    query=query.strip()
    results=wikipedia.summary(query,sentences=2)
    print(results)
    talk(results)


if __name__ == "__main__":
    #talk("Kaushal")
    #greet()
    while True:
        query=listen().lower()
        if query:
            search(query)

        elif 'exit' in query or 'stop' in query:
            talk("Okay ,Sir! As you say")
            break