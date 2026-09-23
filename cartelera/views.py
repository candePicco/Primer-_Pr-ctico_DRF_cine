from rest_framework import generics

from .models import Butaca, Entrada, Funcion, Pelicula, Sala
from .serializers import (
    ButacaSerializer,
    EntradaSerializer,
    FuncionPublicSerializer,
    FuncionSerializer,
    PeliculaSerializer,
    SalaSerializer,
)


# -------------------- PELÍCULAS --------------------

class PeliculasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class PeliculasDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


# -------------------- SALAS --------------------

class SalasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class SalasDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


# -------------------- BUTACAS --------------------

class ButacasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Butaca.objects.all().select_related("sala")
    serializer_class = ButacaSerializer


class ButacasDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Butaca.objects.all().select_related("sala")
    serializer_class = ButacaSerializer


# -------------------- FUNCIONES --------------------

class FuncionesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Funcion.objects.all().select_related("pelicula", "sala")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FuncionPublicSerializer
        else:
            return FuncionSerializer


class FuncionesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcion.objects.all().select_related("pelicula", "sala")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FuncionPublicSerializer
        else:
            return FuncionSerializer


# -------------------- ENTRADAS --------------------

class EntradasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Entrada.objects.all().select_related(
        "funcion",
        "funcion__pelicula",
        "butaca",
    )
    serializer_class = EntradaSerializer


class EntradasDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrada.objects.all().select_related(
        "funcion",
        "funcion__pelicula",
        "butaca",
    )
    serializer_class = EntradaSerializer