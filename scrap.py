from re import split
from bs4 import BeautifulSoup
import requests
import mysql.connector 

sql_user = {
            'user':'Gabriel', 
            'password':'Tg@briel10',
            'host':'127.0.0.1',
            'port':'3306',
            'database':'web'}

cnx =  mysql.connector.connect(**sql_user)

cursor = cnx.cursor()

def scrap():

    for articles in stxt.find_all('article'):

        titles = articles.h2.a.text

        url = articles.h2.a['href']

        summary = articles.p.text

        download = articles.find('footer',class_='entry-footer cf').a['href']

        cursor.execute("insert into webscraping(url,url_down,tittle,summary) values ('{0}','{1}','{2}','{3}');".format(url,download,titles,summary))

        print(titles,'\n',url,'\n',summary,'\n',download,'\n\n',page_i)

        cnx.commit()

page_i = 1

site = requests.get("https://baixarmusica.me/page/{}/".format(page_i)).text

stxt = BeautifulSoup(site,'lxml')

last_page = stxt.find("a", class_='last')['href']

final_page = int(last_page.split('/',5)[4])

while page_i <= final_page:
    site = requests.get("https://baixarmusica.me/page/{}/".format(page_i)).text
    stxt = BeautifulSoup(site,'lxml')
    scrap()
    page_i = page_i + 1

cursor.close()
cnx.close()
