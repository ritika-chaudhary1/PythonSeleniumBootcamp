from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(5)

driver.find_element(
    By.CSS_SELECTOR, 
    "input[name= 'username']"
            ).send_keys("tomsmith")

driver.find_element(
    By.CSS_SELECTOR,
    "input[name= 'password']"
).send_keys("SuperSecretPassword!")

driver.find_element(
    By.CSS_SELECTOR,
    "button.radius"
).click()

time.sleep(3)

print(driver.title)
driver.quit()