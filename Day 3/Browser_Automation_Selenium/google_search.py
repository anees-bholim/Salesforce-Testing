from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
print("Google Opened")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Trailhead")

time.sleep(2)

search_box.submit()
print("Search Completed")

time.sleep(5)

driver.quit()