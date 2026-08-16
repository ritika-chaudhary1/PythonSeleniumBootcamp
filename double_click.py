from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://api.jquery.com/dblclick/")

time.sleep(3)

# Switch to the iframe containing the demo
iframe = driver.find_element(By.TAG_NAME, "iframe")

driver.switch_to.frame(iframe)

# Find the box
box = driver.find_element(By.TAG_NAME, "div")

# Create ActionChains
actions = ActionChains(driver)

# Double-click
actions.double_click(box).perform()

time.sleep(3)

driver.quit()