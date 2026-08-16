from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/hovers")

time.sleep(3)

# Find all elements with class "figure"
user = driver.find_elements(By.CLASS_NAME, "figure")[0]

# Create ActionChains
actions = ActionChains(driver)

# Move mouse over the first image
actions.move_to_element(user).perform()

time.sleep(3)

driver.quit()