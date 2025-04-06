from pydantic import BaseModel


class AdditionModel(BaseModel):
    additional_info: str
    additional_number: int
    id: int


class CreateEntityModel(BaseModel):
    title: str
    important_numbers: list[int]
    verified: bool
    addition: AdditionModel


class EntityModel(CreateEntityModel):
    id: int


class UpdateEntityModel(CreateEntityModel):
    pass
