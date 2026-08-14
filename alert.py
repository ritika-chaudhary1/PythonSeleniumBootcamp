# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# time.sleep(3)
# alert = driver.switch_to.alert
# alert.accept()

# time.sleep(3)

# driver.quit()



#for accept alert

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(
    By.XPATH, "//button[text()='Click for JS Alert']"
).click()

alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

print(alert.text)

alert.accept()

time.sleep(3)

driver.quit()


