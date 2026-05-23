from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()


#Get all windows
windows = driver.window_handles


#Switch to windows
driver.switch_to.window(windows[1])

print(driver.title)

time.sleep(5)

driver.quit()