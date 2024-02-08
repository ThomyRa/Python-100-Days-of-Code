from scraper import Scraper
from form_filler import FormFiller


scraper = Scraper()
print(scraper.get_prices())
print(scraper.get_address())
print(scraper.get_links())

addresses = scraper.get_address()
prices = scraper.get_prices()
links = scraper.get_links()

prices = [price.split("/")[0] for price in prices]

form_filler = FormFiller()
for _ in range(len(addresses)):
    form_filler.fill_form(addresses[_], prices[_], links[_])
