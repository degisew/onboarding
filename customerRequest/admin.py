from django.contrib import admin

from .models import CustomerRequest,Company

# Register your models here.


admin.site.register(CustomerRequest)
admin.site.register(Company)