from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    from django.contrib.staticfiles.views import serve
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve),
    ]
