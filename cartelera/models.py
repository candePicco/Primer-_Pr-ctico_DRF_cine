from django.db import models


class Pelicula(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    clasificacion = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)
    fecha_estreno = models.DateField()
    activa = models.BooleanField(default=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo


class Sala(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=100, blank=True)
    capacidad = models.PositiveIntegerField()

    class Meta:
        ordering = ["numero"]

    def __str__(self):
        return self.nombre or f"Sala {self.numero}"


class Butaca(models.Model):
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name="butacas",
    )
    fila = models.CharField(max_length=5)
    numero = models.PositiveIntegerField()

    class Meta:
        ordering = ["sala", "fila", "numero"]
        constraints = [
            models.UniqueConstraint(
                fields=["sala", "fila", "numero"],
                name="butaca_unica_por_sala",
            )
        ]

    def __str__(self):
        return f"{self.fila}{self.numero} - {self.sala}"


class Funcion(models.Model):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        related_name="funciones",
    )
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name="funciones",
    )
    fecha = models.DateField()
    horario = models.TimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["fecha", "horario"]

    def __str__(self):
        return f"{self.pelicula} - {self.fecha} {self.horario}"


class Entrada(models.Model):
    funcion = models.ForeignKey(
        Funcion,
        on_delete=models.CASCADE,
        related_name="entradas",
    )
    butaca = models.ForeignKey(
        Butaca,
        on_delete=models.CASCADE,
        related_name="entradas",
    )
    cliente = models.CharField(max_length=150)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_compra"]
        constraints = [
            models.UniqueConstraint(
                fields=["funcion", "butaca"],
                name="una_entrada_por_butaca_y_funcion",
            )
        ]

    def __str__(self):
        return f"Entrada #{self.pk} - {self.funcion.pelicula} - {self.butaca}"
