from pages.inventory_page import InventoryPage
import pytest
import json

with open("data/project_data.json") as f:
    data = json.load(f)


@pytest.mark.smoke
def test_six_products_load(logged_in_driver):
    inv = InventoryPage(logged_in_driver)
    assert len(inv.get_product_names()) == 6


@pytest.mark.regression
def test_sort_a_to_z(logged_in_driver):
    inv = InventoryPage(logged_in_driver)
    inv.sort_products("az")
    names = inv.get_product_names()
    assert names == sorted(names)


@pytest.mark.regression
def test_sort_z_to_a(logged_in_driver):
    inv = InventoryPage(logged_in_driver)
    inv.sort_products("za")
    names = inv.get_product_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.regression
def test_sort_price_low_to_high(logged_in_driver):
    inv = InventoryPage(logged_in_driver)
    inv.sort_products("lohi")
    prices = inv.get_product_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_price_high_to_low(logged_in_driver):
    inv = InventoryPage(logged_in_driver)
    inv.sort_products("hilo")
    prices = inv.get_product_prices()
    assert prices == sorted(prices, reverse=True)


@pytest.mark.smoke
def test_cart_badge_increments(logged_in_driver):
    inv = InventoryPage(logged_in_driver)
    assert inv.get_cart_count() == 0
    inv.add_to_cart(data["products"][0]["name"])
    assert inv.get_cart_count() == 1
    inv.add_to_cart(data["products"][1]["name"])
    assert inv.get_cart_count() == 2


@pytest.mark.regression
def test_cart_badge_decrements(logged_in_driver):
    inv = InventoryPage(logged_in_driver)
    inv.add_to_cart(data["products"][0]["name"])
    assert inv.get_cart_count() == 1
    inv.remove_from_inventory(data["products"][0]["name"])
    assert inv.get_cart_count() == 0