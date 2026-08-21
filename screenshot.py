from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.google.com")
time.sleep(3)

#screenshot take
driver.save_screenshot("google.png")
print("Screenshot taken and saved successfully")
driver.quit()

