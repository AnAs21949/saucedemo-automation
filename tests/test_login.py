from pages.login_page import LoginPage
import json
import pytest

with open("data/project_data.json") as f:
    test_data = json.load(f)
    data = test_data["valid_credentials"]


@pytest.mark.parametrize("data", data)
def test_valid_login(driver, data):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials(data["user_name"], data["password"])
    login_url = driver.current_url
    assert "inventory" in login_url, "Login failed, not redirected to inventory page"

@pytest.mark.parametrize("data", test_data["invalid_credentials"])
def test_invalid_login(driver, data):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials(data["user_name"], data["password"])
    assert "Epic sadface" in login_page.error_handler(), "Error message not displayed for invalid credentials"



