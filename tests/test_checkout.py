from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
import pytest
import json

with open("data/project_data.json") as f:
    data = json.load(f)


def reach_checkout_step1(driver):
    inv = InventoryPage(driver)
    inv.add_to_cart(data["products"][0]["name"])
    inv.go_to_cart()
    CartPage(driver).go_to_checkout()
    return CheckoutPage(driver)


def reach_checkout_step2(driver):
    checkout = reach_checkout_step1(driver)
    checkout.fill_personal_info(
        data["valid_credentials"][0]["first_name"],
        data["valid_credentials"][0]["last_name"],
        data["valid_credentials"][0]["postal_code"]
    )
    checkout.click_continue()
    return CheckoutOverviewPage(driver)


@pytest.mark.smoke
def test_full_checkout(logged_in_driver):
    overview = reach_checkout_step2(logged_in_driver)
    overview.click_finish_button()
    assert overview.is_on_success_page()


@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.parametrize("case", data["checkout_empty_field_cases"])
def test_empty_field_error(logged_in_driver, case):
    checkout = reach_checkout_step1(logged_in_driver)
    checkout.fill_personal_info(case["first_name"], case["last_name"], case["postal_code"])
    checkout.click_continue()
    assert checkout.has_error()
    assert case["expected_error"] in checkout.get_error_message()


@pytest.mark.regression
def test_cancel_step1_returns_to_cart(logged_in_driver):
    checkout = reach_checkout_step1(logged_in_driver)
    checkout.click_cancel()
    assert "cart.html" in logged_in_driver.current_url


@pytest.mark.regression
def test_price_math(logged_in_driver):
    overview = reach_checkout_step2(logged_in_driver)
    assert overview.total_matches_items_plus_tax()


@pytest.mark.regression
def test_cancel_step2_returns_to_inventory(logged_in_driver):
    overview = reach_checkout_step2(logged_in_driver)
    overview.click_cancel_button()
    assert InventoryPage(logged_in_driver).is_page_loaded()

    