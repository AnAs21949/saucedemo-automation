from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import json
import pytest


with open("data/project_data.json") as f:
    test_data = json.load(f)
    data = test_data["valid_credentials"]

@pytest.mark.parametrize("data", data)
def test_purchase_flow(driver, data):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials(data["user_name"], data["password"])
    
    #inventory page
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart(data["product_name"])
    inventory_page.go_to_cart()

    #cart page
    cart_page = CartPage(driver)
    assert data["product_name"] in cart_page.get_item_name(), "Item not added to cart"
    cart_page.checkout_cart()

    #checkout page
    checkout_page = CheckoutPage(driver)
    checkout_page.checkout_credentials(data["first_name"], data["last_name"], data["postal_code"])
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()
    assert "Thank you for your order!" in checkout_page.get_checkout_message(), "Checkout failed, success message not displayed"
