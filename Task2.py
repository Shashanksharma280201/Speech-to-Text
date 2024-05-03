# !pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://techcrunch.com/2024/04/30/sams-clubs-ai-powered-exit-tech-reaches-20-of-stores/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the main content element
main_content = soup.find('div', class_='article-content')

# Extract the text content
text_content = main_content.get_text()

# Print the text content
print(text_content)
