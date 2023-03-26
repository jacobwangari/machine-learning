import requests
import csv
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'http://tatuatatu.co.ke/results'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element
table = soup.find('table')

# Find all rows in the table and store them in a list
rows = []
for i , row in enumerate(table.find_all('tr')):
    if i <= 7:
        rows.append([cell.text.strip() for cell in row.find_all('td')])

# Write the data to a CSV file in UTF-8 encoding
with open('input.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

