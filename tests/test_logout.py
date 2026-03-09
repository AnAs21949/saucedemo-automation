import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_logout_redirects_to_login(logged_in_driver):
    inv = InventoryPage(logged_in_driver)
    inv.logout()
    assert "inventory" not in logged_in_driver.current_url


