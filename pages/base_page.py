
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

with open ("data/config.json") as f:
    config = json.load(f)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config["timeout"])
    
    def open(self, url):
        self.driver.get(url)
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def type(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))