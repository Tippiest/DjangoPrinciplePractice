from django.contrib import admin
from .models import Customer, Logger, Menu, Vehicle
from .models import MenuCategory

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Logger)