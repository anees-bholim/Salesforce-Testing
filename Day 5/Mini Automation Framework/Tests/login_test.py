from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By

driver = get_driver

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")

driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit]").click()

print("Login Successful")

driver.quit()