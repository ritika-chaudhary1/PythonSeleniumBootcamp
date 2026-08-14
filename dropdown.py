#method 1 (by visible text)

from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = driver.find_element(By.ID, "dropdown")
select = Select(dropdown)

#select option1
select.select_by_visible_text("Option 1")
time.sleep(2)

#select option2
select.select_by_visible_text("Option 2")

print(select.first_selected_option.text)

time.sleep(2)

print(driver.title)
driver.quit()
