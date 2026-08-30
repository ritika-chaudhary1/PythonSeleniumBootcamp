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

# Wait until username field exists
username = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)

username.send_keys("tomsmith")

print("Username entered successfully")

driver.quit()