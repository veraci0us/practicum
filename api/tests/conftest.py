import pytest

from api.config.consts import TEST_ENTITIES_NUM
from api.services.entities.base_methods import BaseMethods
from api.services.entities.payloads import entity_payload


def get_test_entity_id(init_base_methods):
    _, new_entity_id = init_base_methods.create_entity(entity_payload)
    return new_entity_id


@pytest.fixture()
def init_base_methods():
    return BaseMethods()


# create 1 random entity and return id
@pytest.fixture()
def entity_id(init_base_methods):
    return get_test_entity_id(init_base_methods)

# create and delete 1 test entity


@pytest.fixture()
def handle_db_data(db_cleanup, init_base_methods):
    entity_id = get_test_entity_id(init_base_methods)
    yield entity_id
    db_cleanup(entity_id)

# delete 1 test entity


@pytest.fixture()
def db_cleanup(init_base_methods):
    def cleanup(entity_id):
        init_base_methods.delete_entity((entity_id))

    return cleanup


@pytest.fixture()
def handle_multiple_entities(init_base_methods):
    test_entities = []

    for num in range(TEST_ENTITIES_NUM):
        _, id = init_base_methods.create_entity(entity_payload)
        _, new_entity = init_base_methods.get_entity(id)
        test_entities.append(new_entity)

    yield test_entities

    for test_entity in test_entities:
        init_base_methods.delete_entity(test_entity['id'])
