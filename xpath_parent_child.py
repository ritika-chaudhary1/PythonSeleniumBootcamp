from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")

# Locate the login form
form = driver.find_element(
    By.XPATH,
    "//form[@id='login']"
)

# Find username input inside the form
username = form.find_element(
    By.XPATH,
    ".//input[@id='username']"
)

username.send_keys("tomsmith")

print("Username found using parent-child relationship")

driver.quit()