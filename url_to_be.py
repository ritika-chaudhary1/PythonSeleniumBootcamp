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

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

driver.find_element(
    By.CSS_SELECTOR,
    "button[type='submit']"
).click()

# Wait for exact URL
wait.until(
    EC.url_to_be("https://the-internet.herokuapp.com/secure")
)

print("Exact URL verified successfully")
print("Current URL:", driver.current_url)

driver.quit()
