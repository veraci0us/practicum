import allure

from api.services.entities.entity_model import EntityModel
from api.services.entities.payloads import entity_payload
from api.utils.add_property import add_property
from api.utils.api_method import HttpCodes


class TestUpdateEntity:
    @allure.suite("API Tests")
    @allure.feature('Update entity')
    def test_update_entity(self, entity_id, init_base_methods, db_cleanup):
        with allure.step('Create test entity'):
            update_payload = entity_payload
        with allure.step('Update test entity'):
            status_code = init_base_methods.update_entity(
                entity_id, update_payload)

        with allure.step('Check if status code is 204'):
            assert status_code == HttpCodes.NoContent

        with allure.step('Get updated entity'):
            _, found = init_base_methods.get_entity(entity_id)

        with allure.step('Verify fields'):
            assert EntityModel(**found)

        updated_with_id = add_property([
            {'property': 'id', 'value': entity_id, 'root': True},
            {'property': 'id', 'value': entity_id,
             'root': False, 'nest': 'addition'}
        ], update_payload)

        with allure.step('Check if found entity is the updated one'):
            assert found == updated_with_id

        with allure.step('Delete test entity'):
            db_cleanup(entity_id)
