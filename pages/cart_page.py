
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CartPage(BasePage):
    cart_item = (By.CLASS_NAME, "cart_item")
    inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")

    def get_item_name(self):
        product_names = []
        products = self.find_elements(self.cart_item)
        for product in products:
            product_names.append(self.get_text(self.inventory_item_name))
        return product_names
    
    def checkout_cart(self):
        self.click(self.checkout_button)