
import requests
from bs4 import BeautifulSoup

# Function to fetch and parse the webpage
def fetch_news(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    else:
        print("Failed to retrieve the page")
        return None

# Function to extract news headlines
def extract_headlines(soup):
    headlines = []
    for item in soup.find_all("a", class_="sdc-site-tile__headline-link"):
        headlines.append(item.get_text(strip=True))
    return headlines
