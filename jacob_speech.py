import pyttsx3 as p 
import pyjokes
import datetime
import time


engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hour():
    h = datetime.datetime.now().hour
    if h >= 1 and h< 12:
        speak("Good Morning Sir !")
    elif h >= 12 and h < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good evening sir !")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    hour()
    speak("Welcome back!")
    #speak("Today's date is")
    #date()
    speak("Jacob at your service. How can I help you sir ?")

def my_skills():
    speak("Sir I can play videos on youtube, search the web for you, give you weather reports, tell you jokes, and the list goes on")
    speak("My developers are currently working on embedding IOT features in me as well. Hope you enjoy my services")

def bad_words():
    speak("Sir Please Don't abuse. I am sorry if I said something wrong ")

def jokes():
    speak(pyjokes.get_joke(language='en',category='neutral'))

def thankYou():
    speak("It's my pleasure to help you sir!")
    