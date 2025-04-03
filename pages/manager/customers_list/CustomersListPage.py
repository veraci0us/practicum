from selenium.webdriver.common.by import By

from helpers.math import calc_average, count_letters, find_closest_index
from pages.base.BasePage import BasePage


class CustomersListPage(BasePage):

    TABLE_BODY = (
        By.CSS_SELECTOR,
        "table.table-bordered.table-striped > tbody")
    TABLE_ROW = (By.CSS_SELECTOR, 'tr')
    TABLE_CELL = (By.CSS_SELECTOR, 'td')
    FIRST_COLUMN = (By.CSS_SELECTOR, 'td:nth-child(1)')
    FIRST_NAME_LINK = (
        By.CSS_SELECTOR,
        '.ng-scope table thead tr td:first-child a')
    CARET_DOWN = (By.CSS_SELECTOR, 'span.fa.fa-caret-down')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[ng-model="searchCustomer"]')
    DELETE_BTN = (By.CSS_SELECTOR, 'button[ng-click="deleteCust(cust)"]')

    def __init__(self, driver):
        super().__init__(driver)

    def customer_added(self, customer):
        table_body = self.get_present_element(self.TABLE_BODY)
        last_row = table_body.find_elements(*self.TABLE_ROW)[-1]
        cells = last_row.find_elements(*self.TABLE_CELL)

        actual_data = [cell.text.strip() for cell in cells[:3]]
        # post code to num
        actual_data = {
            'name': actual_data[0],
            'last_name': actual_data[1],
            'post_code': int(actual_data[2])
        }

        return actual_data == customer

    def click_name_link(self):
        self.click(self.FIRST_NAME_LINK)

    def sort_by_name(self):
        self.click_name_link()
        caret_down = self.get_present_element(self.CARET_DOWN)
        caret_class = caret_down.get_attribute('class')

        if 'ng-hide' in caret_class:
            self.click_name_link()
        else:
            return

    def get_all_names(self):
        table_body = self.get_present_element(self.TABLE_BODY)
        rows = table_body.find_elements(*self.TABLE_ROW)
        names = []
        print(len(rows))
        for row in rows:
            print(row.get_attribute('outerHTML'))
            first_col = row.find_element(*self.FIRST_COLUMN)
            names.append(first_col.text.strip())
        return names

    def is_sorted_ascen(self):
        names = self.get_all_names()
        return names == sorted(names)

    def calc_name_for_deletion(self):
        names = self.get_all_names()
        letters_in_words = count_letters(names)
        average = calc_average(letters_in_words)
        index_of_closest = find_closest_index(letters_in_words, average)

        return names[index_of_closest]

    def search(self, value):
        self.add_text(self.SEARCH_INPUT, value)

    def is_found(self, name):
        names = self.get_all_names()
        return len(names) == 1 and names[0] == name

    def delete_cust(self):
        self.click(self.DELETE_BTN)

    def is_cust_deleted(self, name):
        names = self.get_all_names()
        return name not in names
