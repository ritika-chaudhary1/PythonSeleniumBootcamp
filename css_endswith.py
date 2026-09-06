from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")

# CSS attribute ends-with selector
username = driver.find_element(
    By.CSS_SELECTOR,
    "input[id$='name']"
)

username.send_keys("tomsmith")

print("Username found using CSS ends-with selector")

driver.quit()