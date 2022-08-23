from django.contrib import admin

from .models import *


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    pass
