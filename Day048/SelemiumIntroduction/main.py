from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

##############################
# Day 47 Challenge solved using Selenium
# URL = "https://www.amazon.com/BINNUNE-Microphone-Playstation-Headphones-Cancelling/dp/B096VRK6J5/133-4732069-7769535"
# driver.get(url=URL)
#
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# Closes a single Tab
# driver.close()
##############################

URL = "https://www.python.org"
driver.get(url=URL)

# Search elements by NAME
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

# Search elements by ID
button = driver.find_element(By.ID, "submit")
print(button.size)

# Search element by CSS_SELECTOR
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.get_attribute("href"))

# Search element by X-PATH
link = driver.find_element(By.XPATH, "/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(link.text)

# Closes the entire Browser
driver.quit()
