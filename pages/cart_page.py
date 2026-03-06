from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    cart_items = (By.CLASS_NAME, "cart_item")
    item_name = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")

    def get_item_name(self):
        products = self.find_elements(self.cart_items)
        return [product.find_element(*self.item_name).text for product in products]

    def checkout_cart(self):
        self.click(self.checkout_button)
