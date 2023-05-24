from django.conf import settings
from django.db.models import CASCADE, CharField, FloatField, ForeignKey, Model


class Farm(Model):
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Field(Model):
    farm = ForeignKey(Farm, on_delete=CASCADE)
    name = CharField(max_length=255)
    usable_area = FloatField()

    def __str__(self):
        return f"{self.farm} - {self.name}"
