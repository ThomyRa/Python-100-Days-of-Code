from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")


class Scraper:

    def __init__(self):
        self.prices = self.get_prices()
        self.addresses = self.get_address()
        self.links = self.get_links()

    def get_prices(self):
        all_prices = soup.select("span.PropertyCardWrapper__StyledPriceLine")
        self.prices = [price.getText().split("+")[0] for price in all_prices]
        return self.prices

    def get_address(self):
        all_addresses = soup.findAll(name="address")
        self.addresses = [address.getText().strip() for address in all_addresses]
        return self.addresses

    def get_links(self):
        all_links = soup.select("a.property-card-link")
        self.links = [link['href'] for link in all_links]
        return self.links