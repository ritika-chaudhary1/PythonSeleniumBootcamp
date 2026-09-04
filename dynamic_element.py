# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install())
# )

# driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# time.sleep(2)

# # Find the input using its stable attribute
# input_box = driver.find_element(
#     By.CSS_SELECTOR,
#     "#input-example input"
# )

# input_box.send_keys("Hello Selenium")
# print("text entered successfully")
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

wait = WebDriverWait(driver, 10)

# Click Enable button
enable_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example button"))
)

enable_button.click()

# Wait until input becomes clickable/enabled
input_box = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input"))
)

input_box.send_keys("Hello Selenium")

print("Text entered successfully")

driver.quit()