from selenium import webdriver 
import re
import nltk
import time



def web(k) :
    driver = webdriver.Chrome()  
    driver.get("https://google.co.in/search?q="+k)
    time.sleep(10)
    driver.quit()          

def youtube(k):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/"+k)
    time.sleep(10)
    driver.quit()


