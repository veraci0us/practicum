from pages.base.BasePage import BasePage
from pages.manager.add_customer.AddCustLocators import AddCustLocators
from helpers.faker_helper import get_random_10_digits, get_random_last_name
from helpers.turn_digit_to_letter import turn_digit_to_letter

class AddCustPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.post_code = get_random_10_digits()
        self.name = turn_digit_to_letter(self.post_code)
        self.last_name = get_random_last_name()

    def fill_post_code(self): 
        print(type(self.post_code))
        self.add_text(AddCustLocators.POST_CODE_FIELD, self.post_code)

    def fill_name(self):
        self.add_text(AddCustLocators.NAME_FIELD, self.name)
    
    def fill_last_name(self):
        self.add_text(AddCustLocators.LAST_NAME_FIELD, self.last_name)

    def submit_customer(self):
        self.click(AddCustLocators.SUBMIT_CUSTOMER_BTN)

    def is_customer_added_alert(self, alert_text):
        alert = self.get_alert_text()
        return alert_text in alert
    
    def get_customer(self):
        return [self.name, self.last_name, self.post_code]