from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    checkout_message = (By.CLASS_NAME, "complete-header")

    def checkout_credentials(self, first_name, last_name, postal_code):
        self.type(self.first_name_input, first_name)
        self.type(self.last_name_input, last_name)
        self.type(self.postal_code_input, postal_code)

    def continue_checkout(self):
        self.click(self.continue_button)

    def finish_checkout(self):
        self.click(self.finish_button)

    def get_checkout_message(self):
        return self.get_text(self.checkout_message)
