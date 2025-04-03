from selenium.webdriver.common.by import By

from pages.base.BasePage import BasePage


class AddCustPage(BasePage):

    NAME_FIELD = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[ng-model="lName"]')
    POST_CODE_FIELD = (By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    SUBMIT_CUSTOMER_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)

    def fill_post_code(self, post_code):
        self.add_text(self.POST_CODE_FIELD, post_code)

    def fill_name(self, name):
        self.add_text(self.NAME_FIELD, name)

    def fill_last_name(self, last_name):
        self.add_text(self.LAST_NAME_FIELD, last_name)

    def submit_customer(self):
        self.click(self.SUBMIT_CUSTOMER_BTN)

    def is_customer_added_alert(self, alert_text):
        alert = self.get_alert_text()
        return alert_text in alert
