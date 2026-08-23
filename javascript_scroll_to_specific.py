from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/large")

time.sleep(2)

#find an element near the bottom
element = driver.find_element(By.ID, "page-footer")

#scroll to that element
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(3)

print("scrolled to the specific element successfully")
driver.quit()