from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(2)

# Get the full path of test.txt
file_path = os.path.abspath("test.txt")

#find file upload input
upload = driver.find_element(By.ID, "file-upload")

#send file path
upload.send_keys(file_path)
time.sleep(3)

#click upload button
driver.find_element(By.ID, "file-submit").click()
time.sleep(3)

print("File uploaded successfully!")
driver.quit()
