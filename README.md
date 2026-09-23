# Cine API - Práctico Django REST Framework
RAMIREZ PI

API REST para administrar la cartelera de un cine.

## Entidades

- Películas
- Salas
- Butacas
- Funciones
- Entradas

El CRUD está implementado con vistas funcionales de Django REST Framework usando `@api_view`.

## Requisitos

- Python 3.11 o superior
- `uv`

## Instalación

```bash
uv sync
```

## Crear la base de datos

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

## Ejecutar el servidor

```bash
uv run python manage.py runserver
```

Servidor local:

```text
http://127.0.0.1:8000/
```

## Endpoints

| Recurso | Listar / Crear | Ver / Editar / Eliminar |
|---|---|---|
| Películas | `/api/peliculas/` | `/api/peliculas/<id>/` |
| Salas | `/api/salas/` | `/api/salas/<id>/` |
| Butacas | `/api/butacas/` | `/api/butacas/<id>/` |
| Funciones | `/api/funciones/` | `/api/funciones/<id>/` |
| Entradas | `/api/entradas/` | `/api/entradas/<id>/` |

### Métodos

- `GET /api/peliculas/` -> listar
- `POST /api/peliculas/` -> crear
- `GET /api/peliculas/1/` -> consultar una
- `PUT /api/peliculas/1/` -> editar
- `DELETE /api/peliculas/1/` -> eliminar

El mismo esquema se utiliza para los demás recursos.

## Datos de ejemplo

### 1. Crear película

`POST /api/peliculas/`

```json
{
  "titulo": "Intensamente 2",
  "genero": "Animación",
  "duracion": 96,
  "clasificacion": "ATP",
  "descripcion": "Película animada familiar.",
  "fecha_estreno": "2026-08-20",
  "activa": true
}
```

### 2. Crear sala

`POST /api/salas/`

```json
{
  "numero": 1,
  "nombre": "Sala Principal",
  "capacidad": 60
}
```

### 3. Crear butaca

`POST /api/butacas/`

```json
{
  "sala": 1,
  "fila": "A",
  "numero": 1
}
```

### 4. Crear función

`POST /api/funciones/`

```json
{
  "pelicula": 1,
  "sala": 1,
  "fecha": "2026-08-28",
  "horario": "21:30:00",
  "precio": "8000.00"
}
```

### 5. Crear entrada

`POST /api/entradas/`

```json
{
  "funcion": 1,
  "butaca": 1,
  "cliente": "Juan Pérez"
}
```

La API evita vender dos veces la misma butaca para una misma función y verifica que la butaca pertenezca a la sala donde se proyecta la función.