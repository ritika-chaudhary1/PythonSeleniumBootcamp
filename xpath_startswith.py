from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")

# Find username using starts-with()
username = driver.find_element(
    By.XPATH,
    "//input[starts-with(@id, 'user')]"
)

username.send_keys("tomsmith")

print("Username found using XPath starts-with()")

driver.quit()