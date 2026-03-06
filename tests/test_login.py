from pages.login_page import LoginPage


def test_valid_login(driver):
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials("standard_user", "secret_sauce")
    login_url = driver.current_url
    assert "inventory" in login_url, "Login failed, not redirected to inventory page"

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login_credentials("user", "secret_sauce")
    assert "Epic sadface" in login_page.error_handler(), "Error message not displayed for invalid credentials"



