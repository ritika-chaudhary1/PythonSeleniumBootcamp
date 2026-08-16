from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(3)

#get main window handle
main_window = driver.current_window_handle
print("Main Window:", main_window)

# Click on the link to open a new window
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)

#Get all window Handles
all_windows = driver.window_handles
print("All Windows:", all_windows)

#switch to the new tab
driver.switch_to.window(all_windows[1])
print("New tab title:", driver.title)
time.sleep(3)

#switch back to main tab
driver.switch_to.window(main_window)
print("Main tab title:", driver.title)
time.sleep(3)

driver.quit()

