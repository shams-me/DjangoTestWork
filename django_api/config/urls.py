import os

import rest_framework
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("med.api.urls")),
]

if os.environ.get("DEBUG") == "True":
    urlpatterns.extend(
        [
            path("__debug__/", include("debug_toolbar.urls")),
        ]
    )
