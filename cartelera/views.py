from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Butaca, Entrada, Funcion, Pelicula, Sala
from .serializers import (
    ButacaSerializer,
    EntradaSerializer,
    FuncionSerializer,
    PeliculaSerializer,
    SalaSerializer,
)


# -------------------- PELÍCULAS --------------------

@api_view(["GET", "POST"])
def peliculas_lista(request):
    if request.method == "GET":
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        return Response(serializer.data)

    serializer = PeliculaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def pelicula_detalle(request, pk):
    try:
        pelicula = Pelicula.objects.get(pk=pk)
    except Pelicula.DoesNotExist:
        return Response(
            {"error": "Película no encontrada."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        return Response(PeliculaSerializer(pelicula).data)

    if request.method == "PUT":
        serializer = PeliculaSerializer(pelicula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    pelicula.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------- SALAS --------------------

@api_view(["GET", "POST"])
def salas_lista(request):
    if request.method == "GET":
        salas = Sala.objects.all()
        return Response(SalaSerializer(salas, many=True).data)

    serializer = SalaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def sala_detalle(request, pk):
    try:
        sala = Sala.objects.get(pk=pk)
    except Sala.DoesNotExist:
        return Response(
            {"error": "Sala no encontrada."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        return Response(SalaSerializer(sala).data)

    if request.method == "PUT":
        serializer = SalaSerializer(sala, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    sala.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------- BUTACAS --------------------

@api_view(["GET", "POST"])
def butacas_lista(request):
    if request.method == "GET":
        butacas = Butaca.objects.select_related("sala").all()
        return Response(ButacaSerializer(butacas, many=True).data)

    serializer = ButacaSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except IntegrityError:
            return Response(
                {"error": "Esa butaca ya existe en la sala."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def butaca_detalle(request, pk):
    try:
        butaca = Butaca.objects.get(pk=pk)
    except Butaca.DoesNotExist:
        return Response(
            {"error": "Butaca no encontrada."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        return Response(ButacaSerializer(butaca).data)

    if request.method == "PUT":
        serializer = ButacaSerializer(butaca, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response(
                    {"error": "Esa butaca ya existe en la sala."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    butaca.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------- FUNCIONES --------------------

@api_view(["GET", "POST"])
def funciones_lista(request):
    if request.method == "GET":
        funciones = Funcion.objects.select_related("pelicula", "sala").all()
        return Response(FuncionSerializer(funciones, many=True).data)

    serializer = FuncionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def funcion_detalle(request, pk):
    try:
        funcion = Funcion.objects.get(pk=pk)
    except Funcion.DoesNotExist:
        return Response(
            {"error": "Función no encontrada."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        return Response(FuncionSerializer(funcion).data)

    if request.method == "PUT":
        serializer = FuncionSerializer(funcion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    funcion.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------- ENTRADAS --------------------

@api_view(["GET", "POST"])
def entradas_lista(request):
    if request.method == "GET":
        entradas = Entrada.objects.select_related(
            "funcion", "funcion__pelicula", "butaca"
        ).all()
        return Response(EntradaSerializer(entradas, many=True).data)

    serializer = EntradaSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except IntegrityError:
            return Response(
                {"error": "Esa butaca ya fue vendida para esta función."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def entrada_detalle(request, pk):
    try:
        entrada = Entrada.objects.get(pk=pk)
    except Entrada.DoesNotExist:
        return Response(
            {"error": "Entrada no encontrada."},
            status=status.HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        return Response(EntradaSerializer(entrada).data)

    if request.method == "PUT":
        serializer = EntradaSerializer(entrada, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response(
                    {"error": "Esa butaca ya fue vendida para esta función."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    entrada.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
