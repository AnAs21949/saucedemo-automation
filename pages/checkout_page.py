

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name_input =(By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name") 
        self.postal_code_input = (By.ID, "postal-code")
        self.checkout_message = (By.CLASS_NAME, "complete-header")
        self.continue_button = (By.ID, "continue")
       
    def checkout_credentials(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.user_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
    
    def continue_checkout(self):
        self.driver.find_element(*self.continue_button).click()
    
    def finish_checkout(self):
        self.driver.find_element(By.ID, "finish").click()

    def get_checkout_message(self):
        return (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.checkout_message))).text
