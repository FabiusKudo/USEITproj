import requests
from bs4 import BeautifulSoup
import os

# URL of the webpage containing the <a> tag
url = 'https://hackaton2024.useitapps.com/f081ced9-2c7b-4505-973a-630979eb8100'

# Fetch the webpage content
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the <a> tag with the href attribute
    link = soup.find('a', href=True)

    # If the link is found and contains a valid href
    if link and link['href']:
        # Extract the href value (relative path to CSV file)
        csv_file_url = link['href']
        print(f"CSV file found: {csv_file_url}")
        
        # Now, fetch the CSV file
        # Construct the full URL for the CSV file if it's a relative path
        csv_file_url = requests.compat.urljoin(url, csv_file_url)
        
        # Download the CSV file
        csv_response = requests.get(csv_file_url)

        if csv_response.status_code == 200:
            # Save the CSV file locally
            with open('data.csv', 'wb') as f:
                f.write(csv_response.content)
            print("CSV file downloaded successfully!")
        else:
            print(f"Failed to download the CSV file. Status code: {csv_response.status_code}")
    else:
        print("No valid CSV link found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
