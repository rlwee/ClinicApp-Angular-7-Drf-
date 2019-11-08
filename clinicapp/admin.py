from django.contrib import admin
from .models import (Clients, 
                     Schedule, 
                     Employee, 
                     Workload, 
                     Sales)

# Register your models here.

admin.site.register(Clients)
admin.site.register(Schedule)
admin.site.register(Employee)
admin.site.register(Workload)
admin.site.register(Sales)