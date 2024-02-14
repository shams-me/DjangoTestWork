from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from med.api.v1.serializer import EmployeeSerializer, DateSerializer
from med.api.v1.views.mixin import OrderStatsMixIn
from med.models import Employee


class ListEmployeeView(OrderStatsMixIn[Employee], ListAPIView):
    serializer_class = EmployeeSerializer
    model = Employee

    def get(self, request, format=None, *args, **kwargs):
        date_serializer = DateSerializer(data=self.request.query_params)
        if not date_serializer.is_valid():
            return Response(status=400, data={"message": "Invalid query parameters:Check params month and year"})

        queryset = self.get_queryset()
        serialized_employees = self.serializer_class(queryset, many=True)
        return Response(serialized_employees.data)


class EmployeeView(OrderStatsMixIn[Employee], APIView):
    serializer_class = EmployeeSerializer
    model = Employee

    def get(self, request, format=None, *args, **kwargs):
        date_serializer = DateSerializer(data=self.request.query_params)
        if not date_serializer.is_valid():
            return Response(status=400, data={"message": "Invalid query parameters:Check params month and year"})

        try:
            queryset = self.get_queryset().get(id=kwargs.get("pk"))
        except:
            return Response(status=404, data={"message": "Employee not found"})

        serialized_employees = self.serializer_class(queryset, many=False)
        return Response(serialized_employees.data)
