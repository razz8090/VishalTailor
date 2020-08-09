from django.contrib import admin

from .models import Administator, Shirt_de, Pant_de, Cust_info, Employee, Emp_Record
# Register your models here.

admin.site.register(Administator)
admin.site.register(Shirt_de)
admin.site.register(Pant_de)
admin.site.register(Cust_info)
admin.site.register(Employee)
admin.site.register(Emp_Record)