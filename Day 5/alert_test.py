from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascripts_alerts")

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()

time.sleep(3)

driver.quit()