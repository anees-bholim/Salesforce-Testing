from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

#Enter Username
driver.find_element(By.ID, "username").send_keys("tomsmith")

#Enter Password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

#Click Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

success_message = driver.find_element(By.ID, "flash").text

assert "You logged into a secure area!" in success_message

print("Test Passed")

time.sleep(5)

driver.quit()