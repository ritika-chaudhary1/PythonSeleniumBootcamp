from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(3)
    #intentionally trying to find a non-existing element to create a failure
    driver.find_element(By.ID, "wrong_username")


except Exception as e:
    print("Test Failed")
    print("Taking screenshot....")

    driver.save_screenshot("login_failure.png")
    print("screenshot saved successfully")
    
finally:
    driver.quit()




   

