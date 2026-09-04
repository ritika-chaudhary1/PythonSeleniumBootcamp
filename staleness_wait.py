#This is useful when an element disappears from the DOM or is replaced after an action.


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

#store the current content element
element = driver.find_element(
    By.CSS_SELECTOR,
    "#content .row:nth-child(1)"
)

#click refresh
driver.find_element(
    By.CSS_SELECTOR, "a[href='/dynamic_content?with_content=static']"
).click()

#wait until the old element becomes stale
wait.until(
    EC.staleness_of(element)
)

print("Old element became stale successfully")
driver.quit()