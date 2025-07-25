import csv
import requests
from bs4 import BeautifulSoup

# Define the search URL on Societe.com
search_url = 'https://www.societe.com/cgi-bin/search?champs={}&format=&nom=&etat=&region=&departement=&commune=&code_naf=&date_debut=&date_fin=&recherche='

# Open the CSV file and read the rows
with open('20230109_public_ofs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    # Loop over each row in the CSV file
    for row in reader:
        # Extract the SIREN number from the row
        siren = row['siren']

        # Send a request to Societe.com and retrieve the HTML content
        response = requests.get(search_url.format(siren))
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the link to the company's page on Societe.com
        company_link = None
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and 'societe.com/societe/' in href:
                company_link = href
                break

        # If the link to the company's page was found, follow it and scrape the contact information
        if company_link:
            company_response = requests.get(company_link)
            company_soup = BeautifulSoup(company_response.content, 'html.parser')

            # Find the email address in the contact information
            email = None
            for contact in company_soup.find_all('div', {'class': 'coordonnees'}):
                if 'Email' in contact.text:
                    email = contact.find('a').text.strip()
                    break

            # Print the company name and email address
            if email:
                company_name = row['denomination']
                print(company_name, email)
