import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver import ActionChains
from dotenv import load_dotenv
from selenium.common import exceptions
import time
import pdb

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
# driver.delete_all_cookies()

wait = WebDriverWait(driver, 10)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3809745637&distance=25.0&f_AL=true&f_E=2&f_WT=2&geoId=100876405&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER"
driver.get(url=URL)

load_dotenv()

signin_btn = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".nav__button-secondary")))
# pdb.set_trace()
signin_btn.click()

email = wait.until(ec.visibility_of_element_located((By.ID, "username")))
email.send_keys(os.getenv("EMAIL"))

password = wait.until(ec.visibility_of_element_located((By.ID, "password")))
password.send_keys(os.getenv("PASSWORD"))

sign_in = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".btn__primary--large")))
sign_in.click()

job_list = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "li div.job-card-container--clickable")))
pdb.set_trace()
# print(f"The number of jobs found are: {len(job_list)}")
python_jobs = 0
for job in job_list:
    job_title = job.text.split("\n")[0]
    print(job_title)
    if "python" in job_title.lower():
        job.click()
        # time.sleep(1)
        save_job = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".jobs-save-button")))
        save_job.click()
        python_jobs += 1

    scroll_origin = ScrollOrigin.from_element(job)
    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 50) \
        .perform()
    # time.sleep(1)
    new_job = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "li div .job-card-container--clickable")))
    if new_job[-1] not in job_list:
        job_list.append(new_job[-1])
print(f"The total jobs found were: {len(job_list)}")
print(f"The total Python jobs found were: {python_jobs}")
# pdb.set_trace()

