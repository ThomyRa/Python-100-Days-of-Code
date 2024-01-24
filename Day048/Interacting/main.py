from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url=URL)

####################################
# Clicking on a link
# art_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# art_count.click()

####################################
# Finding elements by LINK TEXT
# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

####################################
# Finding the "Search" <input> by NAME
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)

driver.quit()
