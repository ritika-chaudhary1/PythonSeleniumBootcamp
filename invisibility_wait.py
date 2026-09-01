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
wait =WebDriverWait(driver, 10)

#wait for start button
start_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
)
start_button.click()

#wait until loading element disappears
wait.until(
    EC.invisibility_of_element_located((By.ID, "loading"))
)
print("loading disappeared successfully")

#wait for final result
message = wait.until(
    EC.visibility_of_element_located((By.ID, "finish"))
)
print("Message:", message.text)
driver.quit()
