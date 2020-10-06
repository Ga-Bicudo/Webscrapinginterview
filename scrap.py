from bs4 import BeautifulSoup
import requests

site = requests.get('https://baixarmusica.me').text

stxt = BeautifulSoup(site,'lxml')

for articles in stxt.find_all('article'):

    titles = articles.h2.a.text

    url = articles.h2.a['href']

    summary = articles.p.text

    download = articles.find('footer',class_='entry-footer cf').a['href']

    print(titles,'\n',url,'\n',summary,'\n',download,'\n\n')