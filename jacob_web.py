from selenium import webdriver
import re
import nltk
import time

stopword = nltk.corpus.stopwords.words("english")


def web(k):
    driver = webdriver.Chrome("C:/Users/Anu-PC/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver.exe")
    driver.get("https://google.co.in/search?q=" + k)
    time.sleep(10)
    driver.quit()


def youtube(k):
    driver = webdriver.Chrome("C:/Users/Anu-PC/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver.exe")
    driver.get("https://www.youtube.com/" + k)
    time.sleep(10)
    driver.quit()


def flipkart(query):

    list = re.split("\W+", query)
    text = [word for word in list if word not in stopword]
    driver = webdriver.Chrome("C:/Users/Anu-PC/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver.exe")
    text.remove("order")
    text.remove("Flipkart")
    keyword = ' '.join(map(str, text))
    driver.get("https://www.flipkart.com/search?q=" + keyword)
    time.sleep(15)
    driver.quit()


def amazon(query):
    list = re.split("\W+", query)
    text = [word for word in list if word not in stopword]
    driver = webdriver.Chrome("C:/Users/Anu-PC/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver.exe")
    text.remove("order")
    text.remove("Amazon")
    keyword = ' '.join(map(str, text))
    driver.get("https://www.amazon.in/s?k=" + keyword)
    time.sleep(15)
    driver.quit()
    # https://www.amazon.in/s?k=
