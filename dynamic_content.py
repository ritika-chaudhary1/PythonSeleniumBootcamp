from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/dynamic_content")

wait = WebDriverWait(driver, 10)

# Get the first content row
row = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content .row")
    )
)
old_text = row.text
print("Old content:", old_text)

#refresh the dynamic content
driver.find_element(
    By.CSS_SELECTOR,
    "a[href*='dynamic_content']"
).click()

#wait until the old element is no longer attached to the DOM
wait.until(
    EC.staleness_of(row)
)

print("Old element became stale successfully")

#find the new element
new_row = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#content .row")
    )
)

print("New content:", new_row.text)
driver.quit()
