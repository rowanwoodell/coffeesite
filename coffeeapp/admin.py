from django.contrib import admin

from .models import Coffee, Roaster, TastingNote, Country

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Roaster)
admin.site.register(TastingNote)
admin.site.register(Country)