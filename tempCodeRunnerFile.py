
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