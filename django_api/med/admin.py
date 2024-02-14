from django.contrib import admin

from med.models import Client, Employee, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ("full_name",)
    list_filter = ("created", "modified")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ("full_name",)
    list_filter = ("created", "modified")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("created", "modified")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("client", "employee", "price", "created", "modified")
    list_filter = ("created", "modified")
