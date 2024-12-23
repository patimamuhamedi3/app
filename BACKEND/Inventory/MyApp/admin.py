from django.contrib import admin
from .models import Product, Supplier, Warehouse, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Warehouse)
admin.site.register(Order)