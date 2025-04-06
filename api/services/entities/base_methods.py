from api.services.entities.endpoints import EntitiesEndpoints
from api.utils.api_method import Headers, HttpMethods, create_request


class BaseMethods:
    def create_entity(self, new_entity):
        response = create_request(
            url=EntitiesEndpoints.create_entity,
            method=HttpMethods.POST,
            headers=Headers.JSON,
            json=new_entity
        )

        return response.status_code, response.json()

    def get_entity(self, id):
        response = create_request(
            url=EntitiesEndpoints.get_entity(id),
            method=HttpMethods.GET
        )

        return response.status_code, response.json()

    def get_all_entities(self):
        response = create_request(
            url=EntitiesEndpoints.get_entities,
            method=HttpMethods.GET
        )

        return response.status_code, response.json()['entity']

    def delete_entity(self, id):
        response = create_request(
            url=EntitiesEndpoints.delete_entity(id),
            method=HttpMethods.DELETE
        )

        return response.status_code

    def update_entity(self, id, updated_entity):
        response = create_request(
            url=EntitiesEndpoints.update_entity(id),
            method=HttpMethods.PATCH,
            headers=Headers.JSON,
            json=updated_entity
        )

        return response.status_code
