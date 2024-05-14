from django.contrib import admin
from .models import *

# Register your models here.
    
admin.site.register(EstadoRegistro)
admin.site.register(Programa)
admin.site.register(Curso)
admin.site.register(Modulo)
admin.site.register(Examen)
admin.site.register(Pregunta)
admin.site.register(Alternativa)
admin.site.register(Respuesta)
admin.site.register(Matricula)
admin.site.register(RegistroCurso)
admin.site.register(RegistroExamen)
admin.site.register(NotaPrograma)