import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.EXPLICIT_WAIT)

    def open(self, url):
        logger.info(f"Navigating to {url}")
        self.driver.get(url)

    def click(self, locator):
        logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        logger.info(f"Typing into element: {locator}")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        text = self.wait.until(EC.visibility_of_element_located(locator)).text
        logger.debug(f"Got text '{text}' from element: {locator}")
        return text

    def find_elements(self, locator):
        logger.debug(f"Finding elements: {locator}")
        return self.wait.until(EC.presence_of_all_elements_located(locator))
