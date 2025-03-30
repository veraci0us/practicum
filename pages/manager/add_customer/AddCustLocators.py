from selenium.webdriver.common.by import By

class AddCustLocators:
    CUSTOMERS_BTN = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[ng-model="lName"]')
    POST_CODE_FIELD = (By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    SUBMIT_CUSTOMER_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')