import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
from selenium.common import exceptions
import time
import pdb

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
load_dotenv()

wait = WebDriverWait(driver, 10)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3807670270&f_AL=true&f_E=2&f_WT=2&geoId=100876405&keywords=python+developer&location=Colombia&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
driver.get(url=URL)

signin_btn = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".nav__button-secondary")))
# pdb.set_trace()
signin_btn.click()

email = wait.until(ec.visibility_of_element_located((By.ID, "username")))
email.send_keys(os.getenv("EMAIL"))

password = wait.until(ec.visibility_of_element_located((By.ID, "password")))
password.send_keys(os.getenv("PASSWORD"))

sign_in = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".btn__primary--large")))
sign_in.click()

job_list = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "li div .job-card-container--clickable")))
print(f"The number of jobs found are: {len(job_list)}")
for job in job_list:
    print(job.text.split("\n")[0])
    job_title = job.text.split("\n")[0]
    if "python" in job_title.lower():
        job.click()
        time.sleep(2)

        save_job = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".jobs-save-button")))
        save_job.click()
