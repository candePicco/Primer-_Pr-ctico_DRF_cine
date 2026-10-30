from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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

class PeliculaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------- SALAS --------------------

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------- BUTACAS --------------------

class ButacaViewSet(viewsets.ModelViewSet):
    queryset = Butaca.objects.all().select_related("sala")
    serializer_class = ButacaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------- FUNCIONES --------------------

class FuncionViewSet(viewsets.ModelViewSet):
    queryset = Funcion.objects.all().select_related(
        "pelicula",
        "sala",
    )
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FuncionPublicSerializer
        else:
            return FuncionSerializer


# -------------------- ENTRADAS --------------------

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all().select_related(
        "funcion",
        "funcion__pelicula",
        "butaca",
    )
    serializer_class = EntradaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]