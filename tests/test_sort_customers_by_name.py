from pages.manager.ManagerPage import ManagerPage
from pages.manager.customers_list.CustomersListPage import CustomersListPage

class TestSortCustomersByName:
    def test_sort_customers_by_name(self, setup):
        manager_page = ManagerPage(setup)
        customers_list_page = CustomersListPage(setup)

        manager_page.click_customers()
        assert manager_page.matches_endpoint('list')

        customers_list_page.sort_by_name()
        assert customers_list_page.is_sorted_ascen()
    