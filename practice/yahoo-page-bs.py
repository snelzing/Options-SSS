#This is to get the contents of the yahoo page. I will try to have that be the only concern of this file....

import requests
from bs4 import BeautifulSoup 
import lxml

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    print(type(req.text))
    return BeautifulSoup(req.text, 'lxml')

def scrapeYahoo(url):
    bs = getPage(url)
    thing = bs.find
    return thing

print(scrapeYahoo("https://finance.yahoo.com/quote/AAPL/options?p=AAPL"))