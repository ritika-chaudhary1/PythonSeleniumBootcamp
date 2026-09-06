from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/login")

# Start from the child element
username = driver.find_element(
    By.ID,
    "username"
)

# Move from child to parent
parent_form = username.find_element(
    By.XPATH,
    "./parent::div"
)

print("Moved from child to parent successfully")
print("Parent tag:", parent_form.tag_name)

driver.quit()