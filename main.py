import speech_recognition as sr
import webbrowser
import time
import musicLibrary
import requests

import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

newsapikey = "d046e6488e994b55bdfa4c307bac65c3"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):

    if "open google" in c.lower():
         webbrowser.open('https://google.com')
    elif "open youtube" in c.lower():
         webbrowser.open('https://youtube.com')
    elif "open linkedin" in c.lower():
         webbrowser.open('https://linkedin.com')
    elif "open facebook" in c.lower():
         webbrowser.open('https://facebook.com')
    elif c.lower().startswith("play"):
        song = c.lower()[5:].strip()
        if(song in musicLibrary.music):
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak(f"Sorry , song not found")
    elif "news" in c.lower():
        newsapi = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapikey}"
        res = requests.get(newsapi)
        if res.status_code != 200:
            speak("Sorry, I could not fetch the news")
            return
        
        data = res.json()
        for i,article in enumerate(data["articles"][:5],start=1):
            title = article.get("title")
            if title:
                print(f"{i}. {title}")
                speak(title)
                time.sleep(0.6)

    else:
        #let openAI handle it
        

    

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio).lower()
            print(word)
            if("exit" in word or "quit" in word or "stop" in word):
                speak("Goodbye")
                print("Jarvis leaving")
                break
            if("jarvis" in word):
                speak("Yes, I am listening")
                time.sleep(0.9)
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))