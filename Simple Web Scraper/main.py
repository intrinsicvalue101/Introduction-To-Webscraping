# Main Theme: Scraping basic HTML elements (headings, paragraphs, and links) from a webpage using Requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup


# ==============================================================================
# FUNCTION: Basic Web Scraper
# ==============================================================================
def scrape():
    """Sends an HTTP GET request to example.com and extracts key HTML elements."""

    url = 'https://www.scrapethissite.com/pages/simple/'

    # Send an HTTP GET request to the URL and store the response
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract specific elements using CSS selectors
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    # Print out the extracted data
    print(f"Title: {title}")
    print(f"Text: {text}")
    print(f"Link: {link}")


# ==============================================================================
# SCRIPT ENTRY POINT
# ==============================================================================
if __name__ == '__main__':
    # Call the scrape function to execute the process when run directly
    scrape()