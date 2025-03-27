from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.url_helpers import get_endpoint

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def find_el(self, locator):
        return self.wait.until(EC.visibility_of_element_located(*locator), "Element not found")

    def click(self, locator):
        el = self.find_el(*locator)
        el.click()

    def matches_endpoint(self, target_endpoint):
        endpoint = get_endpoint(self.driver.current_url)
        return endpoint == target_endpoint
    
    def add_text(self, locator, text):
        el = self.find_el(*locator)
        el.send_keys(text)