import os

from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pygrunn2023.settings")

from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application

# Only Django:
# application = get_asgi_application()

apps.populate(settings.INSTALLED_APPS)

from pyapp.endpoints import router

application = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")
application.include_router(router, prefix="/api")
application.mount("/", get_asgi_application())
