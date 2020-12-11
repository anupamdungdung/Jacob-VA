from selenium import webdriver 
import re
import nltk
import time

stopword = nltk.corpus.stopwords.words("english")


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

def flipkart(query):
    list = re.split("\W+",query)
    text = [word for word in list if word not in stopword]
    driver = webdriver.Chrome() 
    text.remove("order")
    text.remove("Flipkart")
    keyword = ' '.join(map(str,text)) 
    driver.get("https://www.flipkart.com/search?q="+keyword)
    time.sleep(15)
    driver.quit()

