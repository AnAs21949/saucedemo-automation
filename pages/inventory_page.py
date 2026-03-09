
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    
    cart = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    product_names = (By.CLASS_NAME, "inventory_item_name")
    product_prices = (By.CLASS_NAME, "inventory_item_price")
    open_burger_menu_button = (By.ID, "react-burger-menu-btn")
    close_burger_menu_button = (By.ID, "react-burger-cross-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    
    def is_page_loaded(self) -> bool:
        return "inventory.html" in self.get_current_url()
    
    def add_to_cart(self, product_name):
        item = product_name.replace(" ", "-").lower()
        self.click((By.ID, f"add-to-cart-{item}"))


    def go_to_cart(self):
        self.click(self.cart)

    def sort_products(self, sort_option):
        dropdown = self.wait.until(EC.visibility_of_element_located(self.sort_dropdown))
        Select(dropdown).select_by_value(sort_option)
    
    def get_cart_count(self) -> int:
        if self.is_element_visible(self.cart_badge):
            return int(self.get_text(self.cart_badge))
        return 0
    
    def get_product_names(self):
        return [item.text for item in self.find_elements(self.product_names)]

    def get_product_prices(self):
        return [float(item.text.replace('$', '')) for item in self.find_elements(self.product_prices)]
    
    def remove_from_inventory(self, product_name):
        item = product_name.replace(" ", "-").lower()
        self.click((By.ID, f"remove-{item}"))

    def logout(self):
        self.click(self.open_burger_menu_button)
        self.click(self.logout_link)

    def click_product(self, product_name: str):
        self.click((By.LINK_TEXT, product_name))