from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(5)

driver.find_element(By.NAME, "username").send_keys("tomsmith")

driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")

time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)

print(driver.title)

driver.quit()