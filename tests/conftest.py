import base64
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Browser to run tests on: chrome or firefox (default: chrome)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode (auto-enabled in CI)",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    # Auto-enable headless when running in CI environments
    headless = request.config.getoption("--headless") or bool(os.getenv("CI"))

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        })
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
    else:
        raise ValueError(f"Unsupported browser: '{browser}'. Use 'chrome' or 'firefox'.")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs.get("driver")
            if driver and pytest_html:
                screenshot_b64 = driver.get_screenshot_as_base64()
                html = (
                    '<div><img src="data:image/png;base64,%s" alt="screenshot" '
                    'style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>'
                    % screenshot_b64
                )
                extra.append(pytest_html.extras.html(html))
    report.extras = extra
