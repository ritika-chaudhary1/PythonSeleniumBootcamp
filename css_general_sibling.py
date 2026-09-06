from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")

# Find the Username label
label = driver.find_element(
    By.CSS_SELECTOR,
    "label[for='username']"
)

# Find any input that comes after the label
username = driver.find_element(
    By.CSS_SELECTOR,
    "label[for='username'] ~ input"
)

username.send_keys("tomsmith")

print("Username found using CSS general sibling selector")

driver.quit()