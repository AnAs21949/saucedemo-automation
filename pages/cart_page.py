
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    
    item_name = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")
    cart_items = (By.CLASS_NAME, "cart_item")

    def get_item_name(self):
        product_names = []
        products = self.find_elements(self.cart_items)
        for product in products:
            product_names.append(product.find_element(By.CLASS_NAME, "inventory_item_name").text)
        return product_names
    
    def checkout_cart(self):
        self.click(self.checkout_button)