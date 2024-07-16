import requests
from bs4 import BeautifulSoup
import functions


# Main function
def main():
    url = "https://www.skysports.com/"  # Replace with the actual news website URL
    soup = functions.fetch_news(url)
    if soup:
        headlines = functions.extract_headlines(soup)
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")


if __name__ == "__main__":
    main()
