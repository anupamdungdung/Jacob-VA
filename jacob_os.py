import subprocess
import os
import time
import re
from jacob_speech import*


def openCalculator(query):
    list = re.split("\W+", query)
    text = [word for word in list]
    if 'open' in text:
        try:
            subprocess.Popen('C:/Windows/System32/calc.exe')
            time.sleep(15)
        except Exception as e:
            speak("Error! Could not open calculator")
            print(str(e))

def openNotePad(query):
    list = re.split("\W+", query)
    text = [word for word in list]
    if 'open' in text:
        try:
            subprocess.Popen('C:/Windows/System32/notepad.exe')
            time.sleep(15)

        except Exception as e:
            speak("Error! Could not open Notepad")
            print(str(e))
