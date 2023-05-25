from typing import List

from django.contrib.auth import get_user_model
from fastapi import APIRouter

from .models import Farm, Field
from .schemas import FarmDTO, FieldDTO, ReportDTO

User = get_user_model()

router = APIRouter()

@router.get("/farms", response_model=List[FarmDTO])
def get_farms():
    return list(Farm.objects.all())


@router.get("/farms/{id}", response_model=FarmDTO)
def get_farm_by_id(id: int):
    return Farm.objects.aget(id=id)


@router.get("/fields", response_model=List[FieldDTO])
def get_fields():
    return list(Field.objects.all())


@router.get("/report/{user_id}", response_model=ReportDTO)
async def report(user_id: int):
    return {
        "user": await User.objects.aget(id=user_id),
        "farms": [f async for f in Farm.objects.filter(owner_id=user_id)],
        "fields": [f async for f in Field.objects.filter(farm__owner_id=user_id).select_related("farm")],
    }
