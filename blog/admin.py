from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Kategori)



class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','kategory','date')

admin.site.register(Artikel, ArtikelAdmin)
# Register your models here.

class ResepAdmin(admin.ModelAdmin):
    list_display = ('title','porsi','kunci','waktu','tingkat')

admin.site.register(Resep, ResepAdmin)
