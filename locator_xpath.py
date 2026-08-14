from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

# Username
driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tomsmith")

# Password
driver.find_element(By.XPATH, "//*[@name='password']").send_keys("SuperSecretPassword!")

# Login Button
driver.find_element(By.XPATH, "//*[@type='submit']").click()

time.sleep(3)

print(driver.title)

driver.quit()