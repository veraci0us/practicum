import allure

from helpers.faker_helper import get_random_10_digits, get_random_last_name
from helpers.turn_digit_to_letter import turn_digit_to_letter


class TestAddCustomer:
    @allure.description('Check if new customer is added to the list')
    @allure.feature('Add Customer')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_customer(self, manager_page, add_cust_page,
                          customers_list_page):
        with allure.step('Navigate to addCust page'):
            manager_page.click_add_customer_btn()
            assert manager_page.is_endpoint('addCust')

        post_code = get_random_10_digits()
        name = turn_digit_to_letter(post_code)
        last_name = get_random_last_name()
        with allure.step(f'Fill in {post_code}, {name}, {last_name}'):
            add_cust_page.fill_post_code(post_code)
            add_cust_page.fill_name(name)
            add_cust_page.fill_last_name(last_name)

        with allure.step('Submit new customer'):
            add_cust_page.submit_customer()

        with allure.step('Check alert with message "Customer added successfully"'):
            assert add_cust_page.is_customer_added_alert(
                'Customer added successfully')

        with allure.step('Navigate to customers list'):
            manager_page.click_customers_btn()
            manager_page.matches_endpoint('list')

        with allure.step(f'Check if new customer with name {name}, last name {last_name}, psot code {post_code} is added'):
            assert customers_list_page.customer_added(
                {'name': name, 'last_name': last_name, 'post_code': post_code})
