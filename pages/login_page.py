from selenium.webdriver.common.by import By
from .base_page import BasePage
import config


class LoginPage(BasePage):
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, "//h3[@data-test = 'error']")

    def open(self):
        super().open(config.BASE_URL)

    def enter_login_credentials(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

    def error_handler(self):
        return self.get_text(self.error_message)
