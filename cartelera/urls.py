from django.urls import path

from . import views


urlpatterns = [
    path(
        "peliculas/",
        views.PeliculasListCreateAPIView.as_view(),
        name="peliculas-lista",
    ),
    path(
        "peliculas/<int:pk>/",
        views.PeliculasDetailAPIView.as_view(),
        name="pelicula-detalle",
    ),

    path(
        "salas/",
        views.SalasListCreateAPIView.as_view(),
        name="salas-lista",
    ),
    path(
        "salas/<int:pk>/",
        views.SalasDetailAPIView.as_view(),
        name="sala-detalle",
    ),

    path(
        "butacas/",
        views.ButacasListCreateAPIView.as_view(),
        name="butacas-lista",
    ),
    path(
        "butacas/<int:pk>/",
        views.ButacasDetailAPIView.as_view(),
        name="butaca-detalle",
    ),

    path(
        "funciones/",
        views.FuncionesListCreateAPIView.as_view(),
        name="funciones-lista",
    ),
    path(
        "funciones/<int:pk>/",
        views.FuncionesDetailAPIView.as_view(),
        name="funcion-detalle",
    ),

    path(
        "entradas/",
        views.EntradasListCreateAPIView.as_view(),
        name="entradas-lista",
    ),
    path(
        "entradas/<int:pk>/",
        views.EntradasDetailAPIView.as_view(),
        name="entrada-detalle",
    ),
]