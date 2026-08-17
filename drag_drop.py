from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

time.sleep(3)

# Find source and target
source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

# Create ActionChains
actions = ActionChains(driver)

# Drag A and drop it onto B
actions.drag_and_drop(source, target).perform()

time.sleep(3)

driver.quit()