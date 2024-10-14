from django.contrib import admin
from apps.settings.models import Basesettings,Blog,Employees
# Register your models here.

admin.site.register(Basesettings)
admin.site.register(Blog)
admin.site.register(Employees)