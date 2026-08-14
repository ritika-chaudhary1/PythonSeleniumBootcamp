from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")  
# Click the Confirm button
driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Confirm']"
).click()

# Wait for the alert
alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

# Print alert message
print(alert.text)          #it means cancel the alert

# Click Cancel
alert.dismiss()

driver.quit()