from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tables")

time.sleep(3)

rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

for row in rows:

    if "Smith" in row.text:

        cells = row.find_elements(By.TAG_NAME, "td")

        email = cells[2].text

        print("Actual Email:", email)

        # Verify expected email
        assert email == "jsmith@gmail.com"

        print("Test Passed!")

        break

driver.quit()