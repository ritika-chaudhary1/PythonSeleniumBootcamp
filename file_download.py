from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(2)

# Find the first downloadable file
file_link = driver.find_element(By.CSS_SELECTOR, "#content a")

print("File to download:", file_link.text)

# Click the download link
file_link.click()

time.sleep(5)

print("Download completed")

driver.quit()