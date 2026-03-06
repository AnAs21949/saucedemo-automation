from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    cart = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_name):
        item = product_name.replace(" ", "-").lower()
        self.click((By.ID, f"add-to-cart-{item}"))

    def go_to_cart(self):
        self.click(self.cart)
