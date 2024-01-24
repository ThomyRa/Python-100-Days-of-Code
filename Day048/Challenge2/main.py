from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url=URL)

txt_first_name = driver.find_element(By.NAME, "fName")
txt_first_name.send_keys("First Name")

txt_last_name = driver.find_element(By.NAME, "lName")
txt_last_name.send_keys("Last Name")

txt_email = driver.find_element(By.NAME, "email")
txt_email.send_keys("email@email.com")

btn_signup = driver.find_element(By.TAG_NAME, "button")
btn_signup.click()

# driver.quit()
