import allure

from api.utils.api_method import HttpCodes


class TestDeleteEntity:
    @allure.suite("API Tests")
    @allure.feature('Delete entity')
    def test_delete_entity(self, init_base_methods, entity_id):
        with allure.step('Create a test entity and delete it via DELETE req'):
            status_code = init_base_methods.delete_entity(entity_id)

        with allure.step('Check if status code is 204'):
            assert status_code == HttpCodes.NoContent

        with allure.step('Retrieve deleted entity'):
            status_code, entity = init_base_methods.get_entity(entity_id)

        with allure.step("Check if entity doesn't exist in db"):
            assert status_code == HttpCodes.InternalServerError
            assert entity['error'] == 'no rows in result set'
