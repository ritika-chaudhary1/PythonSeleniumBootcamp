from selenium.webdriver.common.by import By


class LoginPage:
    
    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()