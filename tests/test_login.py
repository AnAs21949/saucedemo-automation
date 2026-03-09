from pages.login_page import LoginPage
import json
import pytest

with open("data/project_data.json") as f:
    test_data = json.load(f)
    data = test_data["valid_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize("data", data)
def test_valid_login(driver, data):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials(data["user_name"], data["password"])
    login_url = driver.current_url
    assert "inventory" in login_url, "Login failed, not redirected to inventory page"

@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize("data", test_data["invalid_credentials"])
def test_invalid_login(driver, data):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials(data["user_name"], data["password"])
    assert "Epic sadface" in login_page.get_error_message(), "Error message not displayed for invalid credentials"


@pytest.mark.regression
@pytest.mark.negative
def test_locked_out_user(driver):
    data = test_data["locked_out_user"]
    login = LoginPage(driver)
    login.open()
    login.enter_login_credentials(data["user_name"], data["password"])
    assert data["expected_error"] in login.get_error_message()


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize("data", test_data["empty_login_cases"])
def test_empty_field_login(driver, data):
    login = LoginPage(driver)
    login.open()
    login.enter_login_credentials(data["user_name"], data["password"])
    assert data["expected_error"] in login.get_error_message()


