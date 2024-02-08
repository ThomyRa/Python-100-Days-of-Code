from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pdb

URL = "https://docs.google.com/forms/d/e/1FAIpQLSdfJPjB3tVD0BisdRLOCa07-TbLzAG2idyEUQXImExKQonP_g/viewform?usp=sf_link"


class FormFiller:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def fill_form(self, address: str, price: str, link: str):
        self.driver.get(URL)
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        input_texts = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.Xb9hP input")))
        input_texts[0].click()
        input_texts[0].send_keys(address)
        input_texts[0].click()
        input_texts[1].send_keys(price)
        input_texts[0].click()
        input_texts[2].send_keys(link)

        btn_send = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
        btn_send.click()

