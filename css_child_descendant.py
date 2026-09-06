from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")

# Find the login form
form = driver.find_element(
    By.CSS_SELECTOR,
    "form#login"
)

# Find username input inside the form
username = form.find_element(
    By.CSS_SELECTOR,
    "input#username"
)

username.send_keys("tomsmith")

print("Username found using CSS descendant selector")

driver.quit()