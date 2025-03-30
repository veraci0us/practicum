from selenium.webdriver.common.by import By

class CustomersListLocators:
    TABLE_BODY = (By.XPATH, "//div[@style='height:250px;']//table[contains(@class, 'table')]/tbody")
    TABLE_ROW = (By.CSS_SELECTOR, 'tr')
    TABLE_CELL = (By.CSS_SELECTOR, 'td')
    FIRST_COLUMN = (By.XPATH, './/td[1]')
    FIRST_NAME_LINK = (By.CSS_SELECTOR, '.ng-scope table thead tr td:first-child a')
    CARET_DOWN = (By.CSS_SELECTOR, 'span.fa.fa-caret-down')
    SEARCH_INPUT = (By.XPATH, '//form//input[@ng-model="searchCustomer"]')
    DELETE_BTN = (By.XPATH, "//td/button")