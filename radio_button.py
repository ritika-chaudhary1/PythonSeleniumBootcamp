from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://demoqa.com/radio-button")
yes = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes.click()

time.sleep(5)

driver.quit()