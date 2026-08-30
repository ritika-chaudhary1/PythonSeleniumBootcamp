from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())

)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
wait = WebDriverWait(driver, 10)

#click start
start_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
)
start_button.click()

#wait until Hello World become visible
message = wait.until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

print("Mesage:", message.text)
driver.quit()