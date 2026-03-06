from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()