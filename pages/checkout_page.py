from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    
    user_name_input =(By.ID, "first-name")
    last_name_input = (By.ID, "last-name") 
    postal_code_input = (By.ID, "postal-code")
    checkout_message = (By.CLASS_NAME, "complete-header")
    continue_button = (By.ID, "continue")
       
    def checkout_credentials(self, first_name, last_name, postal_code):
        self.type(self.user_name_input, first_name)
        self.type(self.last_name_input, last_name)
        self.type(self.postal_code_input, postal_code)

    def continue_checkout(self):
        self.click(self.continue_button)

    def finish_checkout(self):
        self.click((By.ID, "finish"))

    def get_checkout_message(self):
        return self.get_text(self.checkout_message)
