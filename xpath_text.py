# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install())
# )

# driver.get("https://the-internet.herokuapp.com/login")

# username = driver.find_element(
#     By.ID,
#     "username"
# )
# username.send_keys("tomsmith")

# password = driver.find_element(
#     By.ID,
#     "password"
# )
# password.send_keys("SuperSecretPassword!")

# # Find Login button using text-based XPath
# login_button = driver.find_element(
#     By.XPATH,
#     "//button[normalize-space(.)='Login']"
# )

# login_button.click()

# print("Login button found using XPath text()")
# print("Current URL:", driver.current_url)

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

driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# Find Login button using text-based XPath
login_button = driver.find_element(
    By.XPATH,
    "//button[normalize-space(.)='Login']"
)

login_button.click()

# Wait for navigation to complete
wait.until(
    EC.url_to_be("https://the-internet.herokuapp.com/secure")
)

print("Login button found using XPath text()")
print("Current URL:", driver.current_url)

driver.quit()