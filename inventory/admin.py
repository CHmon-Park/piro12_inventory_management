from django.contrib import admin

# Register your models here.
from inventory.models import Opponent, Inventory

admin.site.register(Inventory)
admin.site.register(Opponent)