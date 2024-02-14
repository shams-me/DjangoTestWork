from django.urls import path, include

urlpatterns = [path("v1/", include("med.api.v1.urls"))]
