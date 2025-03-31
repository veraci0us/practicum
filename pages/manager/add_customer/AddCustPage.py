from pages.base.BasePage import BasePage
from pages.manager.add_customer.AddCustLocators import AddCustLocators
from helpers.faker_helper import get_random_10_digits, get_random_last_name
from helpers.turn_digit_to_letter import turn_digit_to_letter

class AddCustPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def gen_data(self):
        post_code = get_random_10_digits()
        name = turn_digit_to_letter(post_code)
        last_name = get_random_last_name()

        return {"post_code": post_code, "name": name, "last_name": last_name}

    def fill_post_code(self, post_code): 
        self.add_text(AddCustLocators.POST_CODE_FIELD, post_code)

    def fill_name(self, name):
        self.add_text(AddCustLocators.NAME_FIELD, name)
    
    def fill_last_name(self, last_name):
        self.add_text(AddCustLocators.LAST_NAME_FIELD, last_name)

    def submit_customer(self):
        self.click(AddCustLocators.SUBMIT_CUSTOMER_BTN)

    def is_customer_added_alert(self, alert_text):
        alert = self.get_alert_text()
        return alert_text in alert
    