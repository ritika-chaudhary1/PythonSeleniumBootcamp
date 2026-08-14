from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.google.com")
time.sleep(3)

print("Title:", driver.title)
print("URL:", driver.current_url)

driver.get("https://www.youtube.com")
time.sleep(5)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(3)

driver.quit()