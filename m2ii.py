
import io
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url0 = "https://www.m2iformation.fr/formations/informatique/"
response0 = requests.get(url0)
html0 = response0.content
soup0 = BeautifulSoup(html0, 'html.parser')
informatqiue = soup0.find_all('p',{'class':'ghost'})
for p in informatqiue:
    a = p.find('a')
    sub = 'pdf/'
    if sub not in a['href']:
        url = 'https://www.m2iformation.fr/' + a['href']
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')


        formations = soup.find_all('div', {'class':'col'})
        formations_list = []
        for formation in formations:
            for article in formation.find_all('article', {'class':"formation listing is_essentiel signika"}):
                for div in article.find_all('div'):
                    for h3 in div.find_all('h3'):
                        a = h3.find('a', href = True)
                        url2 = 'https://www.m2iformation.fr/' + a['href']
                        response2 = requests.get(url2)
                        sleep(10)
                        html2 = response.content

                        soup2 = BeautifulSoup(html2, 'html.parser')
                        descriptions = soup2.find_all('div', {'class':'wrap'})
                        driver = webdriver.Chrome(executable_path=r'C:\Users\Abdel\OneDrive\Documents\Selenium\chromedriver.exe')
                        driver.get(url2)
                        h2_elements = driver.find_elements(By.XPATH, "//h2[@class='h3']")
                        h3_elemnts = driver.find_elements(By.XPATH, "//a[@name='programme']/following-sibling::*")
                        des={}
                        for h2_element in h2_elements:
                            if h2_element.text == "Objectifs pédagogiques":
                                lis = h2_element.find_elements(By.XPATH, "//h2[@class='h3']/following-sibling::ul/li")
                                list = [o.text for o in lis]  
                                des[h2_element.text] = list
                            elif h2_element.text == "Niveau requis":
                                des[h2_element.text] = h2_element.find_element(By.XPATH,"//h2[@class='h3']/following-sibling::p").text
                            elif h2_element.text == "Public concerné":
                                des[h2_element.text] = h2_element.find_element(By.XPATH,"//a[@name='public']/following-sibling::p").text       
                        list2=[]
                        for h3_element in h3_elemnts:
                            list2.append(h3_element.text)
                        des["prog"] = list2
            titre = a['href']
            for article in formation.find_all('article', {'class':"formation listing is_essentiel signika"}):
                for strong in article.find_all('p',{'class': 'price'}):
                    prix = strong.string.replace(u'\xa0', '')  
            for article in formation.find_all('article', {'class':"formation listing is_essentiel signika"}):
                for span in article.find_all('p', {'class': 'note'}):  
                    note = span.get_text()
                    note = note[2:]
            for article in formation.find_all('article', {'class':"formation listing is_essentiel signika"}):
                for p in article.find_all('p', {'class': 'col duree'}):
                    duree = p.get_text().replace(u'\xa0', '')
            for article in formation.find_all('article', {'class':"formation listing is_essentiel signika"}):
                for p in article.find_all('p', {'class': 'col modalite'}):
                    for span in  p.find_all('span'):
                        modalite = span.string +", "+ span.next
            formation_dict = {"titre": titre, "description":des , "prix": prix, "note":note, "durée":duree, "modalite":modalite }
            formations_list.append(formation_dict)
df = pd.DataFrame(formations_list)
df.to_csv('data.csv', index=False)

