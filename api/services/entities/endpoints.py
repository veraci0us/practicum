from api.config.consts import BASE_API


class EntitiesEndpoints:
    create_entity = f"{BASE_API}/api/create"
    get_entities = f"{BASE_API}/api/getAll"

    @staticmethod
    def delete_entity(id):
        return f"{BASE_API}/api/delete/{id}"

    @staticmethod
    def update_entity(id):
        return f"{BASE_API}/api/patch/{id}"

    @staticmethod
    def get_entity(id):
        return f"{BASE_API}/api/get/{id}"
