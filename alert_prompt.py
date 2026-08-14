from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the Prompt button
driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Prompt']"
).click()

# Wait for the alert
alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

# Print alert message
print(alert.text)

# Type text into the prompt
alert.send_keys("Ritika")        #Type "Ritika" inside the alert input box.

# Click OK
alert.accept()

driver.quit()