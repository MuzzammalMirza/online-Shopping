from django.contrib import admin
from .models import Cetagory,Sub_Cetagory,Product,contact_us,Order,Brand

# Register your models here.
admin.site.register(Cetagory)
admin.site.register(Sub_Cetagory)
admin.site.register(Product)
admin.site.register(contact_us)
admin.site.register(Order)
admin.site.register(Brand)
