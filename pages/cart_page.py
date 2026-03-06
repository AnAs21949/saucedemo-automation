from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    item_name = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")

    def get_item_name(self):
        return [item.text for item in self.find_elements(self.item_name)]

    def checkout_cart(self):
        self.click(self.checkout_button)
