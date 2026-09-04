#Selenium receives the locator and finds the element itself.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/checkboxes")

wait = WebDriverWait(driver, 10)

# Select the first checkbox
checkbox = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='checkbox']"
)

if not checkbox.is_selected():
    checkbox.click()

# Wait until the checkbox located by CSS is selected
wait.until(
    EC.element_located_to_be_selected(
        (By.CSS_SELECTOR, "input[type='checkbox']")
    )
)

print("Checkbox located and selected successfully")

driver.quit()