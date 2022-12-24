from profil.models import Profil
from django.contrib import admin
from .models import *
# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'alamat', 'telp')
admin.site.register(Profil,ProfilAdmin)