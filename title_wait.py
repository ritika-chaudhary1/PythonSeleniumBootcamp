from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/")

wait = WebDriverWait(driver, 10)

# Wait until title contains "The Internet"
wait.until(
    EC.title_contains("The Internet")
)

print("Title verified successfully")
print("Page title:", driver.title)

driver.quit()