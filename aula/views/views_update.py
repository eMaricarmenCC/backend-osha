from rest_framework.generics import (
    RetrieveUpdateAPIView
)
from ..serializers import *

# UpdateAPIView

class EstadoRegistroUpdateAPIView(RetrieveUpdateAPIView):
    queryset = EstadoRegistro.objects.all()
    serializer_class = EstadoRegistroSerializer


class EstudianteUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class ProgramaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class CursoUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ModuloUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class ExamenUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer


class PreguntaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class AlternativaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer


class RespuestaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


class MatriculaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class RegistroCursoUpdateAPIView(RetrieveUpdateAPIView):
    queryset = RegistroCurso.objects.all()
    serializer_class = RegistroCursoSerializer


class NotaProgramaUpdateAPIView(RetrieveUpdateAPIView):
    queryset = NotaPrograma.objects.all()
    serializer_class = NotaProgramaSerializer