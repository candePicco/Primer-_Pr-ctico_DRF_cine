from rest_framework.routers import DefaultRouter

from .views import (
    ButacaViewSet,
    EntradaViewSet,
    FuncionViewSet,
    PeliculaViewSet,
    SalaViewSet,
)


router = DefaultRouter()

router.register(
    "peliculas",
    PeliculaViewSet,
    basename="pelicula",
)

router.register(
    "salas",
    SalaViewSet,
    basename="sala",
)

router.register(
    "butacas",
    ButacaViewSet,
    basename="butaca",
)

router.register(
    "funciones",
    FuncionViewSet,
    basename="funcion",
)

router.register(
    "entradas",
    EntradaViewSet,
    basename="entrada",
)

urlpatterns = router.urls