from django.contrib import admin

from .models import Customer, Product, Contract
from CustomerDB.models import ContactInfo, Cluster, Third_party, Version, HardWare, Node, Roles
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Contract)
admin.site.register(ContactInfo)
admin.site.register(Version)
admin.site.register(Cluster)
admin.site.register(Third_party)
admin.site.register(HardWare)
admin.site.register(Node)
admin.site.register(Roles)