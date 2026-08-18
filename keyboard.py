from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

time.sleep(2)

username = driver.find_element(By.ID, "username")

username.send_keys("tomsmith")

# Press TAB to move to password field
username.send_keys(Keys.TAB)

# Type password
driver.switch_to.active_element.send_keys("SuperSecretPassword!")

time.sleep(2)

# Press ENTER
driver.switch_to.active_element.send_keys(Keys.ENTER)

time.sleep(3)

print(driver.title)

driver.quit()