from django.contrib import admin
from .models import Entity, Demand, Supplier, SupplierContact, Supply, SupplyRequest
# Register your models here.

admin.site.register(Entity)
admin.site.register(Demand)
admin.site.register(Supplier)
admin.site.register(SupplierContact)
admin.site.register(Supply)
admin.site.register(SupplyRequest)
