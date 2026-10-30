# Cine API - Django REST Framework

**RAMIREZ PICCO**

API REST desarrollada con Django REST Framework para administrar la cartelera de un cine.

El proyecto fue desarrollado de manera progresiva a lo largo de tres prácticos, incorporando modelos relacionados, serializers anidados, vistas basadas en clases, ViewSets, seguridad y autenticación JWT.

---

# Entidades

El sistema cuenta con las siguientes entidades:

- Películas
- Salas
- Butacas
- Funciones
- Entradas

Las entidades se encuentran relacionadas entre sí mediante claves foráneas.

Por ejemplo:

- Una función pertenece a una película.
- Una función se realiza en una sala.
- Una butaca pertenece a una sala.
- Una entrada corresponde a una función y a una butaca.

---

# Práctico 1 - CRUD con `@api_view`

En el primer práctico se desarrolló la estructura inicial de la API REST del cine.

Se implementaron:

- Modelos para la base de datos.
- Serializers mediante `ModelSerializer`.
- Vistas funcionales con `@api_view`.
- Operaciones CRUD.
- Relaciones entre las distintas entidades.
- Validaciones propias del sistema.

## Recursos implementados

- Películas
- Salas
- Butacas
- Funciones
- Entradas

Las vistas permitían realizar:

```text
GET
POST
PUT
DELETE
```

Por ejemplo:

```text
GET /api/peliculas/
POST /api/peliculas/
GET /api/peliculas/1/
PUT /api/peliculas/1/
DELETE /api/peliculas/1/
```

El mismo esquema se utilizó para salas, butacas, funciones y entradas.

## Validaciones

También se incorporaron algunas validaciones propias del sistema.

La combinación de:

```text
función + butaca
```

debe ser única, evitando vender dos entradas para la misma butaca en una función.

Además, antes de crear una entrada se verifica que la butaca seleccionada pertenezca a la misma sala donde se realiza la función.

---

# Práctico 2 - Serializers anidados y vistas basadas en clases

En el segundo práctico se retomó el proyecto anterior y se incorporaron relaciones y funcionalidades propias de Django REST Framework.

Se implementaron:

- Relaciones mediante `ForeignKey`.
- Serializers anidados.
- Concrete Generic API Views.
- `ListCreateAPIView`.
- `RetrieveUpdateDestroyAPIView`.
- Diferentes serializers para lectura y escritura.

## Relación utilizada

Una de las relaciones principales del proyecto es:

```text
Funcion → Pelicula
Funcion → Sala
```

El modelo `Funcion` contiene claves foráneas hacia `Pelicula` y `Sala`.

## Serializer anidado

Se creó un serializer público para funciones:

```python
class FuncionPublicSerializer(serializers.ModelSerializer):
    pelicula = PeliculaSerializer(read_only=True)
    sala = SalaSerializer(read_only=True)
```

De esta manera, una consulta `GET` de funciones devuelve la película y la sala de manera anidada.

Ejemplo:

```json
{
  "id": 2,
  "fecha": "2026-09-20",
  "horario": "19:30:00",
  "precio": "7500.00",
  "pelicula": {
    "id": 3,
    "titulo": "Shrek",
    "genero": "Animación",
    "duracion": 90,
    "clasificacion": "ATP",
    "descripcion": "Película animada de aventura y comedia",
    "fecha_estreno": "2001-05-18",
    "activa": true
  },
  "sala": {
    "id": 1,
    "numero": 1,
    "nombre": "",
    "capacidad": 50
  }
}
```

Para las operaciones de escritura se utiliza `FuncionSerializer`, donde las relaciones se envían mediante sus IDs.

Ejemplo:

```json
{
  "fecha": "2026-09-25",
  "horario": "22:00:00",
  "precio": "8500.00",
  "pelicula": 3,
  "sala": 1
}
```

## Concrete Generic Views

Las vistas funcionales del primer práctico fueron reemplazadas por vistas basadas en clases.

Se utilizaron:

```python
generics.ListCreateAPIView
```

para:

```text
GET listado
POST crear
```

y:

```python
generics.RetrieveUpdateDestroyAPIView
```

para:

```text
GET detalle
PUT actualizar
DELETE eliminar
```

También se utilizó `get_serializer_class()` para seleccionar un serializer diferente dependiendo del tipo de operación.

---

# Práctico 3 - ViewSets, Routers, permisos y JWT

En el tercer práctico se reemplazaron las Concrete Generic Views por ViewSets y se agregó seguridad a la API.

Se implementaron:

- `ModelViewSet`.
- `ReadOnlyModelViewSet`.
- `DefaultRouter`.
- Archivo `routers.py`.
- `permission_classes`.
- `IsAuthenticatedOrReadOnly`.
- Autenticación JWT mediante `djangorestframework-simplejwt`.
- Obtención y renovación de tokens.
- Pruebas mediante Thunder Client.

---

# ViewSets

## Películas

Se utiliza:

```python
class PeliculaViewSet(viewsets.ReadOnlyModelViewSet):
```

Por lo tanto, las películas son un recurso de solo lectura.

Permite:

```text
GET /api/peliculas/
GET /api/peliculas/<id>/
```

No permite:

```text
POST
PUT
PATCH
DELETE
```

## Salas

Utiliza:

```python
viewsets.ModelViewSet
```

Permite CRUD completo.

## Butacas

Utiliza:

```python
viewsets.ModelViewSet
```

Permite CRUD completo.

## Funciones

Utiliza:

```python
viewsets.ModelViewSet
```

Además, utiliza diferentes serializers según la operación.

Para:

```text
list
retrieve
```

se utiliza:

```python
FuncionPublicSerializer
```

Para crear o modificar:

```python
FuncionSerializer
```

## Entradas

Utiliza:

```python
viewsets.ModelViewSet
```

Permite CRUD completo y conserva las validaciones desarrolladas en los prácticos anteriores.

---

# Routers

Los ViewSets se registran mediante `DefaultRouter` en:

```text
cartelera/routers.py
```

Recursos registrados:

```text
peliculas
salas
butacas
funciones
entradas
```

El router genera automáticamente las rutas correspondientes.

La raíz de la API se encuentra en:

```text
http://127.0.0.1:8000/api/
```

---

# Seguridad

Los ViewSets utilizan:

```python
permission_classes = [IsAuthenticatedOrReadOnly]
```

Esto significa que:

- Los métodos de lectura `GET` pueden utilizarse sin autenticación.
- Las operaciones de escritura requieren un usuario autenticado.

Operaciones protegidas:

```text
POST
PUT
PATCH
DELETE
```

---

# Autenticación JWT

La API utiliza:

```text
djangorestframework-simplejwt
```

La autenticación JWT está configurada en `settings.py` mediante:

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

## Obtener token

Endpoint:

```text
POST /api/token/
```

Ejemplo de body:

```json
{
  "username": "usuario",
  "password": "contraseña"
}
```

La respuesta contiene:

```json
{
  "refresh": "...",
  "access": "..."
}
```

El token `access` se utiliza como Bearer Token para acceder a las operaciones protegidas.

---

# Renovar token

Endpoint:

```text
POST /api/token/refresh/
```

Body:

```json
{
  "refresh": "TOKEN_REFRESH"
}
```

Este endpoint devuelve un nuevo `access token`.

---

# Pruebas de seguridad

Las pruebas fueron realizadas utilizando **Thunder Client**.

## Escritura sin autenticación

Se realizó:

```text
POST /api/funciones/
```

sin enviar token.

Resultado:

```text
401 Unauthorized
```

Esto demuestra que `permission_classes` está funcionando.

## Escritura con JWT

Se realizó la misma petición utilizando un `access token` válido como Bearer Token.

Resultado:

```text
201 Created
```

La función fue creada correctamente.

## ReadOnlyModelViewSet

También se intentó:

```text
POST /api/peliculas/
```

utilizando un token válido.

Resultado:

```text
405 Method Not Allowed
```

Esto confirma que `PeliculaViewSet` funciona como `ReadOnlyModelViewSet`.

---

# Endpoints

| Recurso | Listado | Detalle |
| --- | --- | --- |
| Películas | `/api/peliculas/` | `/api/peliculas/<id>/` |
| Salas | `/api/salas/` | `/api/salas/<id>/` |
| Butacas | `/api/butacas/` | `/api/butacas/<id>/` |
| Funciones | `/api/funciones/` | `/api/funciones/<id>/` |
| Entradas | `/api/entradas/` | `/api/entradas/<id>/` |

Endpoints JWT:

| Acción | Endpoint |
| --- | --- |
| Obtener token | `/api/token/` |
| Renovar token | `/api/token/refresh/` |

---

# Ejemplos

## Crear función

```text
POST /api/funciones/
```

Requiere autenticación JWT.

```json
{
  "fecha": "2026-10-30",
  "horario": "20:00:00",
  "precio": "9000.00",
  "pelicula": 3,
  "sala": 1
}
```

## Crear entrada

```text
POST /api/entradas/
```

```json
{
  "funcion": 1,
  "butaca": 1,
  "cliente": "Juan Pérez"
}
```

## Crear sala

```text
POST /api/salas/
```

```json
{
  "numero": 1,
  "nombre": "Sala Principal",
  "capacidad": 60
}
```

## Crear butaca

```text
POST /api/butacas/
```

```json
{
  "sala": 1,
  "fila": "A",
  "numero": 1
}
```

---

# Requisitos

- Python 3.11 o superior
- Django
- Django REST Framework
- `djangorestframework-simplejwt`
- `uv`

---

# Instalación

Instalar las dependencias:

```bash
uv sync
```

---

# Base de datos

Crear las migraciones:

```bash
uv run python manage.py makemigrations
```

Aplicarlas:

```bash
uv run python manage.py migrate
```

---

# Crear usuario

Para probar la autenticación JWT se puede crear un superusuario:

```bash
uv run python manage.py createsuperuser
```

---

# Ejecutar servidor

```bash
uv run python manage.py runserver
```

Servidor:

```text
http://127.0.0.1:8000/
```

API:

```text
http://127.0.0.1:8000/api/
```

---

# Organización en GitHub

El proyecto fue desarrollado utilizando ramas para conservar cada etapa.

```text
main
└── Práctico 1

practico-2
└── Práctico 2

practico-3
└── Práctico 3
```

De esta manera se puede consultar la evolución del proyecto a lo largo de los tres prácticos.