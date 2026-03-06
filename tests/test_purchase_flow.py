from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_purchase_flow(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials("standard_user", "secret_sauce")
    
    #inventory page
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()

    #cart page
    cart_page = CartPage(driver)
    assert "Sauce Labs Backpack" in cart_page.get_item_name(), "Item not added to cart"
    cart_page.checkout_cart()

    #checkout page
    checkout_page = CheckoutPage(driver)
    checkout_page.checkout_credentials("John", "Doe", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()
    assert "Thank you for your order!" in checkout_page.get_checkout_message(), "Checkout failed, success message not displayed"
