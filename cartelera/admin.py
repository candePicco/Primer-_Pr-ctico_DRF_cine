from django.contrib import admin

from .models import Butaca, Entrada, Funcion, Pelicula, Sala


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "genero", "duracion", "clasificacion", "fecha_estreno", "activa")
    list_filter = ("genero", "clasificacion", "activa")
    search_fields = ("titulo",)


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("numero", "nombre", "capacidad")


@admin.register(Butaca)
class ButacaAdmin(admin.ModelAdmin):
    list_display = ("fila", "numero", "sala")
    list_filter = ("sala",)


@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ("pelicula", "sala", "fecha", "horario", "precio")
    list_filter = ("fecha", "sala")


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "funcion", "butaca", "fecha_compra")
    search_fields = ("cliente",)
