from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")

editor = driver.find_element(By.ID, "tinymce")

editor.clear()

editor.send_keys("Automation Testing")

time.sleep(5)

driver.quit()