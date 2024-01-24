from selenium import webdriver
from selenium.webdriver.common.by import By
from prettyprinter import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://www.python.org"
driver.get(url=URL)

raw_event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery li time")
event_dates = [event.get_attribute("datetime").split("T")[0] for event in raw_event_dates]
print(event_dates)

raw_event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery li a")
event_names = [event.text for event in raw_event_names]
print(event_names)

events = {}
for i in range(len(event_names)):
    events[i] = {
        "time": event_dates[i],
        "name": event_names[i]
    }

pprint(events)



# events_info = dict(zip(event_dates, event_names))
# pprint(events_info)

# events = {}
# for i in range(len(events_info)):
#     events[f"{i}"] = events_info[i]
# pprint(events)

driver.quit()
