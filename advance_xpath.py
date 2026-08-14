from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

#usrname using contains

driver.find_element(
    By.XPATH,
      "//*[contains(@id, 'username')]"
      ).send_keys("tomsmith")

# password using AND
driver.find_element(
    By.XPATH,
      "//*[contains(@id, 'password') and @type='password']"
      ).send_keys("SuperSecretPassword!")

# login button using text()
# driver.find_element(
#     By.XPATH,
#       "//*[text()='Login']"
#       ).click()

driver.find_element(
    By.XPATH,
      "//button[@type='submit']"
      ).click()

time.sleep(3)

print(driver.title)

driver.quit()