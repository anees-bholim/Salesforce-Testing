from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/tables")

rows = driver.find_elements(By.XPATH, "//table[@id='table1]/tbody/tr")

print("Total Rows: ", len(rows))

for row in rows:
    print(row.text)
    
time.sleep(5)

driver.quit()