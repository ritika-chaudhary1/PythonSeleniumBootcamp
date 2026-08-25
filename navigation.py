# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.maximize_window()

# # Open first page
# driver.get("https://www.google.com")

# time.sleep(2)

# print("Page 1:", driver.title)

# # Open second page
# driver.get("https://the-internet.herokuapp.com")
# time.sleep(3)
# print("Page 2:", driver.title)

# #go back
# driver.back()
# time.sleep(3)
# print("After Forward:", driver.title)

# #refresh
# driver.refresh()
# time.sleep(3)
# print("After Refresh:", driver.title)

# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

# Open main page
driver.get("https://the-internet.herokuapp.com/")

time.sleep(2)

print("Main Page:", driver.title)

# Click a link
driver.find_element(By.LINK_TEXT, "A/B Testing").click()

time.sleep(2)

print("Second Page:", driver.title)

# Go back
driver.back()

time.sleep(2)

print("After Back:", driver.title)

# Go forward
driver.forward()

time.sleep(2)

print("After Forward:", driver.title)

# Refresh
driver.refresh()

time.sleep(2)

print("After Refresh:", driver.title)

driver.quit()