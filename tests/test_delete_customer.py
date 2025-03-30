from pages.manager.customers_list.CustomersListPage import CustomersListPage
from pages.manager.ManagerPage import ManagerPage

class TestDeleteCust():
    def test_delete_cust(self, setup):
        customers_list_page = CustomersListPage(setup)
        manager_page = ManagerPage(setup)

        manager_page.click_customers()
        assert manager_page.is_endpoint('list')

        target_name = customers_list_page.calc_name_for_deletion()
        customers_list_page.search(target_name)
        assert customers_list_page.is_found(target_name)

        customers_list_page.delete_cust()
        assert customers_list_page.is_cust_deleted(target_name)
        
