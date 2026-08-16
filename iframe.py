from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

# Open iframe practice page
driver.get("https://demoqa.com/frames")

time.sleep(3)

# Find the iframe
iframe = driver.find_element(By.ID, "frame1")

# Switch into the iframe
driver.switch_to.frame(iframe)

time.sleep(2)

# Find the heading inside the iframe
heading = driver.find_element(By.ID, "sampleHeading")

# Print the text
print("Text inside iframe:", heading.text)

time.sleep(3)

# Switch back to the main page
driver.switch_to.default_content()

print("Returned to main page")

time.sleep(2)

driver.quit()