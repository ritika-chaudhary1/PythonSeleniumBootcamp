from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/inputs")

time.sleep(2)

input_box = driver.find_element(By.TAG_NAME, "input")

#enter value
input_box.send_keys("12345")

#get the value using javascript
value = driver.execute_script("return arguments[0].value;", input_box)

print("Input value:", value)
time.sleep(3)
driver.quit()