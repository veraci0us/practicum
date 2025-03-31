from pages.manager.ManagerPage import ManagerPage
from pages.manager.customers_list.CustomersListPage import CustomersListPage
import allure

class TestSortCustomersByName:
    @allure.description('Test sorting customers in ascending order')
    @allure.feature('Sort customers in ascend order')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sort_customers_by_name(self, setup):
        manager_page = ManagerPage(setup)
        customers_list_page = CustomersListPage(setup)

        with allure.step('Navigate to customers list page'):
            manager_page.click_customers()
            assert manager_page.matches_endpoint('list')

        with allure.step('Click Name link in table head to sort in ascen order'):
            customers_list_page.sort_by_name()

        with allure.step('Check if list is sorted'):
            assert customers_list_page.is_sorted_ascen()
    