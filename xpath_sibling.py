from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")

# Start from the Username label
username = driver.find_element(
    By.XPATH,
    "//label[text()='Username']/following-sibling::input"
)

username.send_keys("tomsmith")

print("Username found using following-sibling")

driver.quit()