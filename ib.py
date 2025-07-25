import io
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json
url0 = "https://www.demos.fr/catalogue"
response0 = requests.get(url0)
html0 = response0.content
soup0 = BeautifulSoup(html0, 'html.parser')
informatqiue = soup0.find_all('li',{'class':'courses-course col-md-6'} )
formations_list = []
for p in informatqiue:
    a = p.find('a')
    url = 'https://www.demos.fr' + a['href']
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find_all('span',{'class':'field-content'} )
    for c in info:
        b = c.find('a')
        url2 = 'https://www.demos.fr' + b['href']
        titre1 = b['href']
        response2 = requests.get(url2)
        html2 = response2.content
        soup2 = BeautifulSoup(html2, 'html.parser')
        modalite = soup2.find('li',{'class':'product--modality'} )   
        duree =  soup2.find('li',{'class':'product--duration'} )
        prix =   soup2.find('li',{'class':'product--price'} ) 
        dis = {}
        des = soup2.find_all('div',{'class':'panel panel-default'} ) 
        for d in des:
            for t in d.find_all('a'):
                titre = t.string
            for u in d.find_all('div', {'class':'panel-body'}): 
                dis[titre]= u.get_text().replace('"', '')
                dis[titre] = dis[titre].replace('"', '')
        formation_dict = {"titre": titre1, "description":dis , "prix": prix.text, "note":'', "durée":duree.text, "modalite":modalite.text }
        print(formation_dict)
        formations_list.append(formation_dict)

        


                

