from selenium import webdriver 
import re
import nltk
import time


stopword = nltk.corpus.stopwords.words("english")


def Flipkart() :
    driver = webdriver.Chrome() 
    text.remove("order")
    text.remove("Flipkart")
    keyword = ' '.join(map(str,text))
    driver.get("https://www.flipkart.com/search?q="+keyword) 
    time.sleep(15)
    driver.quit()

def web() :
    driver = webdriver.Chrome()  
    driver.get("https://google.co.in/search?q="+k)
    time.sleep(15)
    driver.quit()

def map() :
    driver = webdriver.Chrome()  
    driver.get("https://www.google.co.in/maps/")
    time.sleep(15)
    driver.quit()    

skill_disctionary = {
    "Flipkart": Flipkart,
    "web": web,
    "maps": map,
    "maps": map
}

text = str(input("Type something...."))
k = text
list = re.split("\W+",text)
text = [word for word in list if word not in stopword]
for i in text:
    if i in skill_disctionary:
        skill_disctionary[i]()
else:
    skill_disctionary["web"]()



