from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com")

time.sleep(2)

#add a cookie
driver.add_cookie({
    "name": "my_cookie",
    "value": "selenium123"
})
print("Cookie added successfully")

#get the cookie just added
cookie = driver.get_cookie("my_cookie")
print("cookie", cookie)
time.sleep(3)

driver.quit()