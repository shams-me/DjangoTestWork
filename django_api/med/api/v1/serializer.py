from rest_framework import serializers


class DateSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    year = serializers.IntegerField()


class BaseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    full_name = serializers.CharField()
    clients_count = serializers.IntegerField()
    products_count = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class EmployeeSerializer(BaseSerializer):
    pass


class ClientSerializer(BaseSerializer):
    pass
