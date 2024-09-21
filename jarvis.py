import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import google.generativeai as genai
import pywhatkit as py

API_KEY = "AIzaSyB5D3iPLpLK2PcZwyu93DnT5PhFS7YWYCk"

def speak(audio):
    initiate = pyttsx3.init()
    initiate.say(audio)
    initiate.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
        print("Good morning")
    elif hour >= 12 and hour < 18:
        print("Good afternoon")
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        print("Good evening")
        speak("Good evening")
    print("Sir, I am Jarvis. How may I help you?")
    speak("Sir, I am Jarvis. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"Atharva: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


wishme()
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'valorant' in query:
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk")
        

    elif "open google" in query:
        webbrowser.open("https://google.com")

    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")

    elif 'Harsh' in query:
        py.sendwhatmsg(f"+919136875629",{query},22,)
        print("Message Sent!")
        speak("Message Sent!")
    elif 'stop' in query:
        break
    else:
        #hand it over to Gemini!
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        try:
            response = model.generate_content(query)
            GeminiResponse = response.text
            GeminiResponse = GeminiResponse.replace("*", "")
            print("Replying...")
            print(f"Gemini: {GeminiResponse}")
            speak(GeminiResponse)
        except Exception as e:
            print("Say that again please...")
                    
