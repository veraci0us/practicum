from pages.base.BasePage import BasePage
from pages.manager.customers_list.CustomersListLocators import CustomersListLocators
from helpers.math import calc_average, find_closest_index, count_letters

class CustomersListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def customer_added(self, customer):
        table_body = self.find_el(CustomersListLocators.TABLE_BODY)
        last_row = table_body.find_elements(*CustomersListLocators.TABLE_ROW)[-1]
        cells = last_row.find_elements(*CustomersListLocators.TABLE_CELL)

        actual_data = [cell.text.strip() for cell in cells[:3]]
        # post code to num
        actual_data[2] = int(actual_data[2])

        return actual_data == customer
    
    def click_name_link(self):
        self.click(CustomersListLocators.FIRST_NAME_LINK)


    def sort_by_name(self):
        self.click_name_link()
        caret_down = self.find_el(CustomersListLocators.CARET_DOWN)
        caret_class = caret_down.get_attribute('class')

        if 'ng-hide' in caret_class:
            self.click_name_link()
        else: 
            return
        
    def get_all_names(self):
        table_body = self.find_el(CustomersListLocators.TABLE_BODY)
        rows = table_body.find_elements(*CustomersListLocators.TABLE_ROW)
        names = []

        for row in rows:
            first_col = row.find_element(*CustomersListLocators.FIRST_COLUMN)
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
        self.add_text(CustomersListLocators.SEARCH_INPUT, value)

    def is_found(self, name):
        names = self.get_all_names()
        return len(names) == 1 and names[0] == name

    def delete_cust(self):
        self.click(CustomersListLocators.DELETE_BTN)
        
    def is_cust_deleted(self, name):
        names = self.get_all_names()
        return name not in names

