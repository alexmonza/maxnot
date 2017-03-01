from django.contrib import admin
from .models import Religion

class ReligionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_religion')

admin.site.register(Religion, ReligionAdmin)

