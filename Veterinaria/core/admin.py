from django.contrib import admin
from .models import Categoria, Mascota
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "observacion", "categoria", "imagen"]
    list_editable = ["observacion"]


admin.site.register(Categoria)
admin.site.register(Mascota,MascotaAdmin)
