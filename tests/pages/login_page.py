from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config.settings import BASE_UI_URL

class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input.button")
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")
    ERROR = (By.CSS_SELECTOR, ".error")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open(self):
        self.driver.get(BASE_UI_URL)

    def login(self, username, password):
        # I use explicit wait to ensure the username field is visible before interacting with it,
        # which helps avoid issues with elements not being ready.
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def is_logged_in(self):
        return len(self.driver.find_elements(*self.LOGOUT_LINK)) > 0

    def error_message(self):
        els = self.driver.find_elements(*self.ERROR)
        return els[0].text if els else ""
