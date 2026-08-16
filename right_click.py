from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

time.sleep(3)

# Find the button
button = driver.find_element(By.CLASS_NAME, "context-menu-one")

# Create ActionChains
actions = ActionChains(driver)

# Right-click
actions.context_click(button).perform()

time.sleep(3)

driver.quit()