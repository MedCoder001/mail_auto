import requests
from bs4 import BeautifulSoup

# Set up the URL and search term
url = 'https://www.example.com/jobs'
search_term = 'Data Scientist'

# Set up the headers to simulate a browser request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# Send a GET request to the URL with the search term in the query string
response = requests.get(url, headers=headers, params={'search_term': search_term})

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the job listings on the page
job_listings = soup.find_all('div', class_='job-listing')

# Loop through each job listing and extract the email address
email_addresses = []
for job_listing in job_listings:
    # Find the email address element within the job listing
    email_element = job_listing.find('a', href=lambda href: href and href.startswith('mailto:'))
    if email_element:
        # Extract the email address from the href attribute
        email_address = email_element['href'].replace('mailto:', '')
        email_addresses.append(email_address)
    if len(email_addresses) >= 500:
        # If we have collected 500 email addresses, break out of the loop
        break

# Print the collected email addresses
print(email_addresses)

# Write the email addresses to a file
with open('email_addresses.txt', 'w') as f:
    for email_address in email_addresses:
        f.write(email_address + '\n')
