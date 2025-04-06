import allure

from api.services.entities.entity_model import EntityModel
from api.utils.api_method import HttpCodes


class TestGetAllEntities:
    @allure.suite("API Tests")
    @allure.feature('Get all entities')
    def test_get_all_entities(self, init_base_methods, handle_multiple_entities):
        with allure.step('Create a list of entities'):
            test_entities = handle_multiple_entities

        with allure.step('Get all entities from db'):
            status_code, all_entities = init_base_methods.get_all_entities()

        with allure.step('Check if status code is OK'):
            assert status_code == HttpCodes.OK

        test_entity_models = [EntityModel(**entity)
                              for entity in test_entities]
        all_entity_models = [EntityModel(**entity) for entity in all_entities]

        with allure.step('Check if created entities list is in db'):
            assert all(
                entity in all_entity_models for entity in test_entity_models)

        with allure.step('Delete test entities'):
            pass
