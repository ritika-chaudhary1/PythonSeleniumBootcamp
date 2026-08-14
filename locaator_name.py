from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(5)

#username
driver.find_element(By.ID, "username").send_keys("tomsmith")

#password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(5)

#login by cclasss name
driver.find_element(By.CLASS_NAME, "radius").click()
time.sleep(5)

print(driver.title)    #to print the title

driver.quit()          #to end or close the browser   
