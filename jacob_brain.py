import speech_recognition as sr
from jacob_web import*
from jacob_speech import*
from jacob_camera import*
from jacob_calculator import*
import sys

wishme()

bad = ["retard","fool","jerk","idiot","wimp","fuck","bimbo","dumb","creepy","weird","fucking","bastard"]


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
                speak("You can wake me up anytime and I will be ready to serve you. Till then take care")
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
                    speak("Today's date is")
                    date()
                elif "skills" in text:
                    my_skills()   
                elif any(x in text for x in bad):
                    bad_words()
                elif "joke" in text:
                    speak("Ha! Ha! Ha!, here goes the joke")
                    jokes()    
                elif "camera" in text:
                    speak("Accessing your device camera")
                    camera()
                elif "Flipkart" in text:
                    speak("Ordering from Flipkart")
                    flipkart(text)
                elif "Amazon" in text:
                    speak("Ordering from Amazon")
                    amazon(text)
                elif "calculator" in text:
                    speak("Opening Calculator")
                    openCalculator()
                elif "thank you" in text:
                    thankYou()
                else:
                    speak("Let me search the web for you sir")
                    web(text)    
        except sr.UnknownValueError:
            speak("Unable to get you !")
            speak("Please say that again")    
    take_command()
    

