from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox1 = driver.find_element(By.XPATH, "//form[@id= 'checkboxes']/input[1]")
checkbox2 = driver.find_element(By.XPATH, "//form[@id= 'checkboxes']/input[2]")

checkbox1.click()
time.sleep(2)

checkbox2.click()
time.sleep(3)

driver.quit()

