from pages.manager.customers_list.CustomersListPage import CustomersListPage
from pages.manager.ManagerPage import ManagerPage
import allure

class TestDeleteCust():
    @allure.description('Test deleting a customer based on name length')
    @allure.feature('Delete customer')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_cust(self, setup):
        customers_list_page = CustomersListPage(setup)
        manager_page = ManagerPage(setup)

        with allure.step('Navigate to customers list page'):
            manager_page.click_customers()
            assert manager_page.is_endpoint('list')

        with allure.step('Search for a name based on math condition'):
            target_name = customers_list_page.calc_name_for_deletion()
            customers_list_page.search(target_name)
            assert customers_list_page.is_found(target_name)

        with allure.step('Hit delete button'):
            customers_list_page.delete_cust()
            assert customers_list_page.is_cust_deleted(target_name)
        
