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

#wait until "hello world!" appears
wait.until(
    EC.text_to_be_present_in_element(
        (By.ID, "finish"),
        "Hello World!")
)

print("Hello World! appeared successfully")
driver.quit()