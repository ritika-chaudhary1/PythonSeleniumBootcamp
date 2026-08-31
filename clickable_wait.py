from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")
wait = WebDriverWait(driver, 10)

#enter username
username = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username.send_keys("tomsmith")

#enter password
password = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password.send_keys("SuperSceretPassword!")

#wait for login button
login_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type= 'submit']"))
)
login_button.click()
print("login button clicked successfully")

driver.quit()