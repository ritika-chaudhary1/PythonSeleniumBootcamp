from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

wait = WebDriverWait(driver, 10)

# Click the button that opens the alert
driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Alert']"
).click()

# Wait until alert appears
wait.until(EC.alert_is_present())

# Switch to alert
alert = driver.switch_to.alert

print("Alert appeared successfully")
print("Alert text:", alert.text)

# Accept alert
alert.accept()

print("Alert accepted successfully")

driver.quit()