#this condition is useful when working with checkboxes,radio buttons, or other selectable elements.

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

# Find the first checkbox
checkbox = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='checkbox']"
)

# Select the checkbox
if not checkbox.is_selected():
    checkbox.click()

#wait until check is selected
wait.until(
    EC.element_to_be_selected(checkbox)
)    

print("checkbox selected successfully")
driver.quit()