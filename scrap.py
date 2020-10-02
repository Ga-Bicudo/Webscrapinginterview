from selenium import webdriver
from bs4 import BeautifulSoup
import requests

site = requests.get('https://baixarmusica.me').text

stxt = BeautifulSoup(site,'lxml')

print(stxt.prettify())