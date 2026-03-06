import pytest
from pages.login_page import LoginPage
import config


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials(config.VALID_USER, config.VALID_PASS)
    assert "inventory" in driver.current_url, "Login failed, not redirected to inventory page"


@pytest.mark.parametrize("username,password,expected_error", [
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
    ("invalid_user",    "wrong_pass",   "Epic sadface"),
    ("standard_user",   "wrong_pass",   "Epic sadface"),
])
def test_invalid_logins(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials(username, password)
    assert expected_error in login_page.error_handler(), (
        f"Expected error '{expected_error}' not shown for user '{username}'"
    )
