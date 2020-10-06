from bs4 import BeautifulSoup
import requests
import mysql.connector 
from selenium.webdriver.chrome.options import Options
from selenium import webdriver 

sql_user = {
            'user':'Gabriel', 
            'password':'Tg@briel10',
            'host':'127.0.0.1',
            'port':'3306',
            'database':'web'}

cnx =  mysql.connector.connect(**sql_user)

cursor = cnx.cursor()

options = webdriver.chrome.options()
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://baixarmusica.me')

last_pag = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/a[4]').click()

print(last_pag)


stxt = BeautifulSoup(site,'lxml')

for articles in stxt.find_all('article'):

    titles = articles.h2.a.text

    url = articles.h2.a['href']

    summary = articles.p.text

    download = articles.find('footer',class_='entry-footer cf').a['href']

    cursor.execute("insert into webscraping(url,url_down,tittle,summary) values ('{0}','{1}','{2}','{3}');".format(url,download,titles,summary))

    print(titles,'\n',url,'\n',summary,'\n',download,'\n\n')

    cnx.commit()

cursor.close()
cnx.close()
