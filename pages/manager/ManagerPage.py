from pages.base.BasePage import BasePage
from pages.manager.ManagerPageLocators import ManagerPageLocators


class ManagerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_add_customer(self):
        self.click(ManagerPageLocators.ADD_CUSTOMER_BTN)
   
    def click_customers(self):
        self.click(ManagerPageLocators.CUSTOMERS_BTN)
    
    def is_endpoint(self, new_endpoint):
        return self.matches_endpoint(new_endpoint)
        
