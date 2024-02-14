from django.urls import path

from .views.client import ClientView
from .views.employee import ListEmployeeView, EmployeeView

urlpatterns = [
    path("employee/statistics", ListEmployeeView.as_view(), name="all employees"),
    path("statistics/employee/<uuid:pk>", EmployeeView.as_view(), name="employee"),
    path("statistics/client/<uuid:pk>", ClientView.as_view(), name="client"),
]
