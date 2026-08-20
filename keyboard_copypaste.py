from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/inputs")
time.sleep(3)

input_box = driver.find_element(By.TAG_NAME, "input")

#type text
input_box.send_keys("Hello Selenium")
time.sleep(3)

#select all text using CTRL + A
input_box.send_keys(Keys.CONTROL, "a")
time.sleep(2)

#copy text using CTRL + C
input_box.send_keys(Keys.CONTROL, "c")
time.sleep(2)

#paste text using CTRL + V
input_box.send_keys(Keys.CONTROL, "v")
time.sleep(2)

print("keyboard copy and paste completed")
driver.quit()
