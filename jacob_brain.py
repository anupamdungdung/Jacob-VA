import speech_recognition as sr
from jacob_web import*
from jacob_speech import*
import sys
import re

wishme()

bad = ["retard","fool","jerk","idiot","wimp","fuck","bimbo","dumb","creepy","weird","fucking"]


while True:
    def take_command():
        r  = sr.Recognizer()
        r.energy_threshold = 1000
        with sr.Microphone() as source:
            print("Listening........")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language = 'en-in')
            print(query) 
            text = query
            if "sleep" in text:
                speak("Ok sir, I am going to sleep")
                sys.exit(1)
            else:
                if "YouTube" in text:
                    if "music" in text:
                        speak("Opening music videos in YouTube")
                        youtube("music")
                    elif "trending" in text:
                        speak("Opening trending videos in YouTube")
                        youtube("trending")
                    elif "gaming" in text:
                        speak("Opening gaming videos in YouTube")
                        youtube("gaming")
                    elif "news" in text:
                        speak("Opening latest news in YouTube")
                        youtube("news")
                    elif "movies" in text:
                        speak("Opening music videos in YouTube")
                        youtube("movies")
                    else:
                        speak("Opening YouTube")
                        youtube("")    
                elif "date" in text:
                    date()
                elif "skills" in text:
                    my_skills()   
                elif any(x in text for x in bad):
                    bad_words()
                elif "joke" in text:
                    speak("Ha Ha, here goes the joke")
                    jokes()    
                else:
                    speak("Let me search the web for you sir")
                    web(text)    
        except sr.UnknownValueError:
            speak("Unable to get you !")
            speak("Please say that again")    
    take_command()
    

