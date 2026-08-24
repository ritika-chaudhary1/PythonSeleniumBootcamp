from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/checkboxes")

time.sleep(2)

#find the first checkbox
checkbox = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0]

#click using javascript
driver.execute_script("arguments[0].click();", checkbox)
time.sleep(3)

print("clicked on the checkbox successfully")
driver.quit()