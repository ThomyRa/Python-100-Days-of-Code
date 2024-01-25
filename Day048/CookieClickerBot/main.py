from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime as dt
from selenium.common import exceptions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=URL)

current_seconds = dt.now().strftime("%S")
print(current_seconds)

counter = 0
while counter <= 2500:
    counter += 1
    cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
    cookie.click()
    current_seconds = dt.now().strftime("%S")
    if int(current_seconds) % 5 == 0:
        print(f"Current second: {current_seconds}")
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
        available_upgrades = [upgrade for upgrade in upgrades if upgrade.get_attribute("class") != "grayed"]
        print(f"El tamaño de la lista es: {len(available_upgrades)}")
        if len(available_upgrades) != 0:
            try:
                upgrade_price = available_upgrades[-1].find_element(By.TAG_NAME, "b").text.split("-")[1].strip().replace(",", "")
                # print(f"Texto>>> {upgrade_price}")
                print(f"The price is: {upgrade_price}")
                money = driver.find_element(By.CSS_SELECTOR, "#money")
                money = int(money.text.replace(",", ""))
                if money >= int(upgrade_price):
                    available_upgrades[-1].click()
                    print(">>> Se hizo click")
                    available_upgrades = []
                    # del available_upgrades[-1]
            except exceptions.NoSuchElementException:
                print("No se encontró el elemento. Continua la ejecución")
                continue

driver.quit()
