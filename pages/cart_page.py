
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_item_name(self):
        product_names = []
        products = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        for product in products:
            product_names.append(product.find_element(By.CLASS_NAME, "inventory_item_name").text)
        return product_names
    
    def checkout_cart(self):
        self.driver.find_element(By.ID, "checkout").click()