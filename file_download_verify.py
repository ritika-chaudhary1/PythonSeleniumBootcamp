from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(2)

# Get the first file name
file_link = driver.find_element(By.CSS_SELECTOR, "#content a")
file_name = file_link.text
print("File to download:", file_name)

#click download
file_link.click()
time.sleep(5)

#check downloads folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_folder, file_name)

#verify file exists
if os.path.exists(file_path):
    print("File downloaded successfully")
    print("File location:", file_path)
else:
    print("File download failed!")
driver.quit()        