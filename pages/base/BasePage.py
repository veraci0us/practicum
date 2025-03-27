from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_el(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator), "Element not found")

    def click(self, locator):
        el = self.find_el(locator)
        el.click()
    
    def add_text(self, locator, text):
        el = self.find_el(locator)
        el.send_keys(text)