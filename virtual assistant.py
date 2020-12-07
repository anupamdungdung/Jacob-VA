import pyttsx3 as p 
import datetime
import time
import speech_recognition as sr
from selenium import webdriver
import re
import nltk

stopword = nltk.corpus.stopwords.words("english")

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
    speak("Jacob at your service. How can i help you sir ?")
wishme()    


def take_command():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(query)
        if 'Flipkart' in query:
            list = re.split("\W+",query)
            text = [word for word in list if word not in stopword]
            driver = webdriver.Chrome() 
            text.remove("order")
            text.remove("Flipkart")
            keyword = ' '.join(map(str,text)) 
            speak("Ordering from Flipkart")
            driver.get("https://www.flipkart.com/search?q="+keyword)
            time.sleep(15)
            driver.quit()
        
        if 'Zomato' in query:
            list = re.split("\W+",query)
            text = [word for word in list if word not in stopword]
            driver = webdriver.Chrome() 
            text.remove("order")
            text.remove("Zomato")
            keyword = ' '.join(map(str,text)) 
            speak("Ordering from Zomato")
            driver.get("https://www.zomato.com/search?q="+keyword)
            time.sleep(15)
            driver.quit()    
        else:
            speak("Let me search the web for you sir")
            driver = webdriver.Chrome()
            k = query
            driver.get("https://google.co.in/search?q="+k)
            time.sleep(15)
            driver.quit()
    except:
        speak("Unable to get you !")
        speak("Please connect to the internet and say that again")
        return "None"

    return query    
take_command()    
 