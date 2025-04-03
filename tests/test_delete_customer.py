import allure


class TestDeleteCust():
    @allure.description('Test deleting a customer based on name length')
    @allure.feature('Delete customer')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_cust(self, manager_page, customers_list_page):

        with allure.step('Navigate to customers list page'):
            manager_page.click_customers_btn()
            assert manager_page.is_endpoint('list')

        target_name = customers_list_page.calc_name_for_deletion()
        with allure.step(f'Search for a {target_name} based on math condition'):
            customers_list_page.search(target_name)
            assert customers_list_page.is_found(target_name)

        with allure.step(f'Hit delete button for {target_name}'):
            customers_list_page.delete_cust()

        with allure.step(f'Verify deletion of {target_name}'):
            assert customers_list_page.is_cust_deleted(target_name)
