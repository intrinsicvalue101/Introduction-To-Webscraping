# Main Theme: Web scraping country data from a sandbox site using Requests and BeautifulSoup

from bs4 import BeautifulSoup as bs
import requests

# ==============================================================================
# SECTION 1: Initialize Request & Parse Webpage Content
# ==============================================================================
# Send an HTTP GET request to the target sandbox website
url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)

# Create a BeautifulSoup object using the HTML parser
soup = bs(response.text, "html.parser")

# ==============================================================================
# SECTION 2: Extracting Single Elements & Testing
# ==============================================================================
# Look at the site title
site_title = soup.find('title').text
print(f"Page Title: {site_title}")

# Find all country container divs on the page
country_all = soup.find_all('div', class_="col-md-4 country")


# ==============================================================================
# SECTION 3: Helper Functions for Extraction
# ==============================================================================

def get_details(country_one):
    """Extracts name, capital, population, and area from a single country container."""
    country_name = country_one.find('h3', class_='country-name').text.strip()
    capital_name = country_one.find('span', class_='country-capital').text
    population = country_one.find('span', class_='country-population').text
    area = country_one.find('span', class_='country-area').text
    return country_name, capital_name, population, area


def get_soup(target_url):
    """Takes a URL, sends a request, and returns a BeautifulSoup object if successful."""
    resp = requests.get(target_url)
    if resp.status_code == 200:
        return bs(resp.text, "html.parser")
    else:
        return None


def get_countries(target_url):
    """Extracts details from all countries listed on the page and returns a list with the total count."""
    page_soup = get_soup(target_url)
    if not page_soup:
        return [], 0

    all_countries = page_soup.find_all('div', class_="col-md-4 country")
    countries_list = []

    for country in all_countries:
        countries_list.append(get_details(country))

    return countries_list, len(countries_list)


# ==============================================================================
# SECTION 4: Execution & Testing
# ==============================================================================
if __name__ == "__main__":
    countries, total_count = get_countries(url)
    print(f"Successfully scraped {total_count} countries.")
    print(f"First country sample: {countries[0] if countries else 'None'}")