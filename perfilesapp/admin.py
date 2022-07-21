from django.contrib import admin

from .models import *


class TiendaActividadAdmin(admin.ModelAdmin):
    list_display=('actividad', 'profesor', 'dias', 'turno', 'precio')
    
admin.site.register(TiendaActividad, TiendaActividadAdmin)
from .models import TiendaActividad

class TiendaObjetosAdmin(admin.ModelAdmin):
    list_display=('producto', 'descripcion', 'precio')
    
admin.site.register(TiendaObjetos, TiendaObjetosAdmin)
from .models import TiendaObjetos

class NosotrosAdmin(admin.ModelAdmin): #cuando lo definamos, como lo diagramariamos, le agregamos la data aca
   pass
    
admin.site.register(Nosotros)
from .models import Nosotros

class SociosAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apellido', 'edad', 'fechanacimiento', 'email')
    
admin.site.register(Socios, SociosAdmin)
from .models import Socios

class ProfesoresAdmin(admin.ModelAdmin):
    list_display=('nombreprofesor', 'apellidoprofesor', 'edadprofesor', 'emailprofesor')
    
admin.site.register(Profesor, ProfesoresAdmin)
from .models import Profesor