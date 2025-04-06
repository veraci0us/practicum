import allure

from api.services.entities.entity_model import EntityModel
from api.utils.api_method import HttpCodes


class TestGetEntity:
    @allure.suite("API Tests")
    @allure.feature('Get entity')
    def test_get_entity(self, init_base_methods, handle_db_data):
        with allure.step('Create test entity'):
            entity_id = handle_db_data

        with allure.step('Get test entity from from db'):
            status_code, entity = init_base_methods.get_entity(entity_id)

        with allure.step('Check if status code is OK'):
            assert status_code == HttpCodes.OK
        with allure.step("Check if entity's fields are correct"):
            assert EntityModel(**entity)

        with allure.step("Check if created entity's id equals the found one"):
            assert EntityModel(**entity).id == entity_id

        with allure.step('Delete test entity'):
            pass
