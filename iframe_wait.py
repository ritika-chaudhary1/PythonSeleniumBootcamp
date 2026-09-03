from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 10)

# Wait for iframe and switch into it
wait.until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr"))
)

print("Switched to iframe successfully")

# Find text inside iframe
editor = wait.until(
    EC.presence_of_element_located((By.ID, "tinymce"))
)

print("Iframe text:", editor.text)

# Switch back to main page
driver.switch_to.default_content()

print("Switched back to main page successfully")

driver.quit()