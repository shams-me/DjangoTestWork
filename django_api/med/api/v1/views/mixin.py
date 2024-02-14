from typing import Generic, TypeVar

from django.db import models
from django.db.models import Sum, Count
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from med.api.v1.serializer import DateSerializer, EmployeeSerializer

ModelType = TypeVar("ModelType", bound=models.Model)


class OrderStatsMixIn(Generic[ModelType]):
    serializer_class = EmployeeSerializer
    http_method_names = ["get"]
    model: ModelType = None
    request: Request

    def get_queryset(self):
        queryset = self.model.objects.filter(
            orders__created__year=int(self.request.query_params.get("year")),
            orders__created__month=int(self.request.query_params.get("month")),
        ).annotate(
            price=Sum("orders__price"),
            clients_count=Count("orders__client", distinct=True),
            products_count=Count("orders__products"),
        )

        return queryset
