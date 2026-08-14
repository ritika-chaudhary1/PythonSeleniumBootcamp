from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(3)

#username by using css id
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
# driver.find_element(By.CSS_SELECTOR, "input[id='username']").send_keys("tomsmith")   it can also wriyte this for call username

#password using css id
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")

#login button using css class
driver.find_element(By.CSS_SELECTOR, ".radius").click()
time.sleep(3)

print(driver.title)

driver.quit()

