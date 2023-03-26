import requests
from bs4 import BeautifulSoup
import csv

# Create a list to store the data
data = []

# Loop through the range of page numbers
for page in range(1, 1000):
    # Construct the URL for the current page
    url = f'http://tatuatatu.co.ke/results/{page}'

    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the table rows in the page
    rows = soup.find_all('tr')

    # Loop through the rows and extract the data
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)

# Save the data to a CSV file with utf-8 encoding
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
