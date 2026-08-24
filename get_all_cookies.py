from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com")

time.sleep(2)
#get all cookies
cookies = driver.get_cookies()
print("All cookies:", cookies)
driver.quit()