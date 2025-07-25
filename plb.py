import io
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
url0 = "https://edugroupe.com/nos-formations/"
response0 = requests.get(url0)
html0 = response0.content
soup0 = BeautifulSoup(html0, 'html.parser')
informatqiue = soup0.find_all('a', href = True )
formations_list = []
for a in informatqiue:
    url = a.get('href')
    word = "https://edugroupe.com/domaine/"
    if word in url:
        u = url
        response = requests.get(u)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find_all('a', href = True)
        for l in info:
            u2 = l.get('href')
            if word in u2:
                u3 = u2
                response1 = requests.get(u)
                html1 = response1.content
                soup1 = BeautifulSoup(html1, 'html.parser')
                info1 = soup1.find_all('a', href = True)
                for l in info1:
                    url2 = l.get('href')
                    word2 = "https://edugroupe.com/domaine/"
                    if word2 in url2:
                        iml = url2
                        response2 = requests.get(iml)
                        html2 = response2.content
                        soup2 = BeautifulSoup(html2, 'html.parser')
                        info2 = soup2.find_all('a',{'class':'formation-link'}, href = True)
                        for h in info2:
                            url3 = h.get('href')
                            prix = soup2.find('div',{'class':'column price'})
                            duree = soup2.find('div',{'class':'column duration'})
                            titre1 = soup2.find('div',{'class':'column formation'})
                            response3 = requests.get(url3)
                            html3 = response3.content
                            soup3 = BeautifulSoup(html3, 'html.parser')
                            info3 = soup3.find_all('div',{'class':'formation_content_item'})
                            dis = {}
                            for t in info3:
                                dis[t.find('h3',{'class':'title'}).text] = t.find('div',{'class':'description'}).text
                            formation_dict = {"titre": titre1.text, "description":dis , "prix": prix.text, "note":'', "durée":duree.text }
                        
                            formations_list.append(formation_dict)
df = pd.DataFrame(formations_list)
print(df)
df.to_csv('data_Edu.csv', index=False)                           
    
                            

    
