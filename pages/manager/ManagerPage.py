from pages.base.BasePage import BasePage
from selenium.webdriver.common.by import By

class ManagerPage(BasePage):

    ADD_CUSTOMER_BTN = (By.CSS_SELECTOR, '[ng-click="addCust()"]')
    CUSTOMERS_BTN = (By.CSS_SELECTOR, '[ng-click="showCust()"]')

    def __init__(self, driver):
        super().__init__(driver)
        
    def click_add_customer_btn(self):
        self.click(self.ADD_CUSTOMER_BTN)
   
    def click_customers_btn(self):
        self.click(self.CUSTOMERS_BTN)
    
    def is_endpoint(self, new_endpoint):
        return self.matches_endpoint(new_endpoint)
        
