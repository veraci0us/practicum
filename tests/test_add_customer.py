from pages.manager.ManagerPage import ManagerPage
from pages.manager.add_customer.AddCustPage import AddCustPage
from pages.manager.customers_list.CustomersListPage import CustomersListPage
import allure

class TestAddCustomer:
    @allure.description('Check if new customer is added to the list')
    @allure.feature('Add Customer')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_customer(self, setup):
        manager_page = ManagerPage(setup)
        add_cust_page = AddCustPage(setup)
        customers_list_page = CustomersListPage(setup)

        with allure.step('Navigate to addCust page'):
            manager_page.click_add_customer()
            assert manager_page.matches_endpoint('addCust')

        with allure.step('Fill in post code, name, last name'):
            add_cust_page.fill_post_code()
            add_cust_page.fill_name()
            add_cust_page.fill_last_name()

        with allure.step('Submit new customer'):   
            add_cust_page.submit_customer()
            assert add_cust_page.is_customer_added_alert('Customer added successfully')

        with allure.step('Navigate to customers list'):
            manager_page.click_customers()
            manager_page.matches_endpoint('list')

        with allure.step('Check if new customer is added'):
            customer = add_cust_page.get_customer()
            assert customers_list_page.customer_added(customer)
            

        




        
        