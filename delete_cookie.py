from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com")

time.sleep(2)

# Add a cookie
driver.add_cookie({
    "name": "my_cookie",
    "value": "selenium123"
})

print("Cookie added")

# Check the cookie
print("Before deleting:", driver.get_cookie("my_cookie"))

# Delete the specific cookie
driver.delete_cookie("my_cookie")

print("Cookie deleted")

# Check again
print("After deleting:", driver.get_cookie("my_cookie"))

time.sleep(2)

driver.quit()