# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.maximize_window()

# driver.get("https://the-internet.herokuapp.com/tables")

# time.sleep(2)

# # Find all rows in the first table
# rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")
# print("Total rows:", len(rows))

# #find all columns in the first row
# columns = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr:first-child td")
# print("Total columns:", len(columns))

# #print first row data
# for column in columns:
#     print(column.text)

#     driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tables")

time.sleep(3)

# Find all rows
rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

print("Total rows:", len(rows))

# Find all columns in the first row
columns = rows[0].find_elements(By.TAG_NAME, "td")

print("Total columns:", len(columns))

# Print the complete first row
print("First row:", rows[0].text)

driver.quit()