from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/large")

time.sleep(2)

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

print("Scrolled to bottom successfully")

driver.quit()
