import subprocess
import os
import time
import re
from jacob_speech import *


def openCalculator(query):
    list = re.split("\W+", query)
    print(list)
    text = [word for word in list]
    print(text)
    if 'open' in text:
        try:
            speak('Opening Calculator')
            subprocess.Popen('C:/Windows/System32/calc.exe')
            time.sleep(15)
        except Exception as e:
            speak("Error! Could not open calculator")
            print(str(e))


def closeCalculator(query):
    list = re.split("\W+", query)
    text = [word for word in list]
    if 'close' in text:
        try:
            speak('Closing Calculator')
            os.system('TASKKILL /F /IM calc.exe')
            time.sleep(15)

        except Exception as e:
            speak("Error! Could not close calculator")
            print(str(e))


def openNotePad(query):
    list = re.split("\W+", query)
    text = [word for word in list]
    if 'open' in text:
        try:
            speak('Opening NotePad')
            subprocess.Popen('C:/Windows/System32/notepad.exe')
            time.sleep(15)

        except Exception as e:
            speak("Error! Could not open Notepad")
            print(str(e))


def closeNotePad(query):
    list = re.split("\W+", query)
    text = [word for word in list]
    if 'close' in text:
        try:
            speak('Closing NotePad')
            os.system('TASKKILL /F /IM notepad.exe')
            time.sleep(15)

        except Exception as e:
            speak("Error! Could not close Notepad")
            print(str(e))
