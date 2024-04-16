from django.contrib import admin
from .models import Datos, Tecnologia, Actividad,  Mensaje

class DatosAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Solo permite la creación de una nueva instancia si aún no existe ninguna
        count = self.model.objects.count()
        if count == 0:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        # Permite editar la instancia existente
        return True


class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'asunto', 'visto')
    readonly_fields = ('nombre', 'asunto','mensaje', 'email')


admin.site.register(Datos, DatosAdmin)
admin.site.register(Tecnologia)
admin.site.register(Actividad)
admin.site.register(Mensaje, MensajeAdmin)

