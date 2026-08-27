from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tables")

time.sleep(3)

# Get all rows
rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

# Search for Smith
for row in rows:

    if "Smith" in row.text:

        print("Found row:")
        print(row.text)

        # Get all cells from this row
        cells = row.find_elements(By.TAG_NAME, "td")

        # Email is the 3rd column
        email = cells[2].text

        print("Email:", email)

        break

driver.quit()