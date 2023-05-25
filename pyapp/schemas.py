from fastapi_utils.api_model import APIModel

# from pydantic import BaseModel

class FarmDTO(APIModel):
    id: int
    name: str


class FieldDTO(APIModel):
    id: int
    name: str
    usable_area: float

class UserDTO(APIModel):
    username: str

class ReportDTO(APIModel):
    user: UserDTO
    farms: list[FarmDTO]
    fields: list[FieldDTO]
