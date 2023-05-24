from fastapi_utils.api_model import APIModel

# from pydantic import BaseModel

class FarmDTO(APIModel):
    id: int
    name: str


class FieldDTO(APIModel):
    id: int
    name: str
    usable_area: float
