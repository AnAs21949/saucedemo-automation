

from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_name):
        item = product_name.replace(" ", "-").lower()
        self.driver.find_element(By.ID, f"add-to-cart-{item}").click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()
