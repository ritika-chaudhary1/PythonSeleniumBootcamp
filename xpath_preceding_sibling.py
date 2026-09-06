from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")

# Start from the Password input
password = driver.find_element(By.ID, "password")

# Move to the previous input using preceding-sibling
username = driver.find_element(
    By.XPATH,
    "//input[@id='password']/preceding-sibling::input[@id='username']"
)

username.send_keys("tomsmith")

print("Moved from password to username using preceding-sibling")

driver.quit()