from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://the-internet.herokuapp.com/windows")

wait = WebDriverWait(driver, 10)

# Store the current window
main_window = driver.current_window_handle

# Click the link that opens a new window
driver.find_element(
    By.LINK_TEXT,
    "Click Here"
).click()

# Wait until two windows are available
wait.until(
    EC.number_of_windows_to_be(2)
)

print("New window opened successfully")

# Get all window handles
windows = driver.window_handles

# Switch to the new window
for window in windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

print("New window title:", driver.title)

# Switch back to main window
driver.switch_to.window(main_window)

print("Main window title:", driver.title)

driver.quit()