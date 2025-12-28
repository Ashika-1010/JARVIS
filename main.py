import speech_recognition as sr
import webbrowser
import time

import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.stop()
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

    print(c)

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
            if("exit" in word or "quit" in word or "stop" in word):
                speak("Goodbye")
                print("Jarvis leaving")
                break
            if("jarvis" in word):
                speak("Ya")
                time.sleep(0.7)
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))