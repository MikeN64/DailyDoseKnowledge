from bs4 import BeautifulSoup as bs4
import re
from Scrape import Scrape

def get_wod_html(word_soup):
    wod_html = word_soup.find('div', class_='wotd-item__definition')
    return wod_html

def get_wod(word_soup):
    wod_html = get_wod_html(word_soup)
    wod = wod_html.find('h1')
    return wod.text

def get_wod_pronunciation(word_soup):
    wod_html = get_wod_html(word_soup)
    wod_pronunciation = wod_html.find(
        'div', class_= 'wotd-item__definition__pronunciation'
        )
    return wod_pronunciation.text.strip()

def get_wod_definition(word_soup):
    wod_html = get_wod_html(word_soup)
    wod_meaning = wod_html.find('div', class_='wotd-item__definition__text')
    return wod_meaning.text.strip()

wod_scraper = Scrape('https://www.dictionary.com/e/word-of-the-day/')
soup = wod_scraper.soup
title = wod_scraper.get_title()
#wod_html = get_wod_html(soup)
wod = get_wod(soup)
wod_pronunciation = get_wod_pronunciation(soup)
wod_meaning = get_wod_definition(soup)

#print(soup)
print('Title: ', title)
#print(wod_html)
print('Word of Day: ', wod)
print('Proninciation: ', wod_pronunciation)
print('Defintion: ', wod_meaning)
