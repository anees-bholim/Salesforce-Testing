from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")

upload = driver.find_element(By.ID, "file-upload")

upload.send_keys("C:/users/Anees/Desktop/test.txt")

driver.find_element(By.ID, "file-submit").click()

print("File uploaded")

time.sleep(5)

driver.quit()