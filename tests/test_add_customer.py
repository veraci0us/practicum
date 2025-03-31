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

        name = add_cust_page.gen_data()['name']
        last_name = add_cust_page.gen_data()['last_name']
        post_code = add_cust_page.gen_data()['post_code']
        with allure.step(f'Fill in {post_code}, {name}, {last_name}'):
            add_cust_page.fill_post_code(post_code)
            add_cust_page.fill_name(name)
            add_cust_page.fill_last_name(last_name)

        with allure.step('Submit new customer'):   
            add_cust_page.submit_customer()

        with allure.step('Check alert with message "Customer added successfully"'):
            assert add_cust_page.is_customer_added_alert('Customer added successfully')

        with allure.step('Navigate to customers list'):
            manager_page.click_customers()
            manager_page.matches_endpoint('list')

        with allure.step(f'Check if new customer with name {name}, last name {last_name}, psot code {post_code} is added'):
            assert customers_list_page.customer_added({'name': name, 'last_name': last_name, 'post_code': post_code})
            

        




        
        