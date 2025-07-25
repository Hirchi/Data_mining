import pandas as pd
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Load CSV file into a pandas DataFrame
df = pd.read_csv('20230109_public_ofs.csv', sep=";")

# Initialize web driver
driver = webdriver.Chrome()

# Loop through rows of DataFrame
for i, row in df.iterrows():
    # Extract relevant company information
    company_name = row['denomination']
    company_address = str(row['adressePhysiqueOrganismeFormation.voie']) + ' ' + str(row['adressePhysiqueOrganismeFormation.codePostal']) + ' ' + str(row['adressePhysiqueOrganismeFormation.ville'])

    
    # Construct search query
    search_query = company_name + ' ' + company_address + ' email'
    
    # Perform Google search
    driver.get('https://www.google.com/search?q=' + search_query)
    time.sleep(1)
    
    # Extract email address from search results
    search_results = driver.find_element(By.CSS_SELECTOR,'div.r')
    email_address = ''
    for result in search_results:
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', result.text):
            email_address = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', result.text).group()
            break
    
    # Update DataFrame with email address
    df.at[i, 'email'] = email_address
    
# Write updated DataFrame back to CSV file
df.to_csv('file_with_emails.csv', index=False)

# Close web driver
driver.quit()
