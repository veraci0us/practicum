from faker import Faker

from api.services.entities.entity_model import CreateEntityModel

faker = Faker()

entity_payload: CreateEntityModel = {
    "addition": {
        "additional_info": faker.sentence(),
        "additional_number": faker.random_number()
    },
    "important_numbers": [faker.random_number() for _ in range(5)],
    "title": faker.sentence(),
    "verified": faker.boolean()
}
