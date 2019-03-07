from bs4 import BeautifulSoup as bs4
import requests

class Scrape():
    def __init__(self, url):
        self.soup = self.get_soup(url)

    def get_soup(self, url):
        source = requests.get(url).text
        soup = bs4(source, features='lxml')
        return soup
    
    def get_title(self):
        title = self.soup.find('title')
        return title.text

