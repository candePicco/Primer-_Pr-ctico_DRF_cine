from django.urls import path

from . import views

urlpatterns = [
    path("peliculas/", views.peliculas_lista, name="peliculas-lista"),
    path("peliculas/<int:pk>/", views.pelicula_detalle, name="pelicula-detalle"),
    path("salas/", views.salas_lista, name="salas-lista"),
    path("salas/<int:pk>/", views.sala_detalle, name="sala-detalle"),
    path("butacas/", views.butacas_lista, name="butacas-lista"),
    path("butacas/<int:pk>/", views.butaca_detalle, name="butaca-detalle"),
    path("funciones/", views.funciones_lista, name="funciones-lista"),
    path("funciones/<int:pk>/", views.funcion_detalle, name="funcion-detalle"),
    path("entradas/", views.entradas_lista, name="entradas-lista"),
    path("entradas/<int:pk>/", views.entrada_detalle, name="entrada-detalle"),
]
