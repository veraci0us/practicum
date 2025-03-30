from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.get_endpoint import get_endpoint
import os
from dotenv import load_dotenv

load_dotenv()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_el(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_els(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        el = self.find_el(locator)
        el.click()
    
    def add_text(self, locator, text):
        el = self.find_el(locator)
        el.send_keys(text)

    def get_alert_text(self):
        alert = self.wait.until(lambda d: d.switch_to.alert)
        alert_text = alert.text
        alert.accept()
        return alert_text 
        
    def get_full_url(self):
        self.wait.until(EC.url_changes(os.getenv('URL')))
        return self.driver.current_url
    
    def matches_endpoint(self, new_endpoint):
        full_url = self.get_full_url()
        endpoint = get_endpoint(full_url)
        return endpoint == new_endpoint
        
    