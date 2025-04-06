import allure

from api.services.entities.entity_model import EntityModel
from api.services.entities.payloads import entity_payload
from api.utils.add_property import add_property
from api.utils.api_method import HttpCodes


class TestCreateEntity:
    @allure.suite("API Tests")
    @allure.feature('Create entity')
    def test_create_entity(self, init_base_methods, db_cleanup):

        with allure.step('Send POST req to create a new entity'):
            new_entity = entity_payload
            post_status_code, new_entity_id = init_base_methods.create_entity(
                new_entity)

        with allure.step('Check if res code is OK'):
            assert post_status_code == HttpCodes.OK

        _, found_entity = init_base_methods.get_entity(new_entity_id)

        with allure.step("Check if created entity's fields are correct"):
            assert EntityModel(**found_entity)

        with_id = add_property([
            {'property': 'id', 'value': new_entity_id, 'root': True},
            {'property': 'id', 'value': new_entity_id,
                'root': False, 'nest': 'addition'}
        ], new_entity)

        with allure.step('Check if created entity equals the initial payload'):
            assert found_entity == with_id

        with allure.step('Delete test entity'):
            db_cleanup(new_entity_id)
