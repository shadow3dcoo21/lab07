from django.contrib import admin
from .models import Usuario, Evento, RegistroEvento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'organizador')
    search_fields = ('nombre', 'fecha')
    list_filter = ('fecha',)

admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(RegistroEvento)
# Register your models here.
