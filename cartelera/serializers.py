from rest_framework import serializers

from .models import Butaca, Entrada, Funcion, Pelicula, Sala


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = "__all__"
        read_only_fields = ["id"]


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = "__all__"
        read_only_fields = ["id"]


class ButacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Butaca
        fields = "__all__"
        read_only_fields = ["id"]


class FuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcion
        fields = "__all__"
        read_only_fields = ["id"]


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = "__all__"
        read_only_fields = ["id", "fecha_compra"]

    def validate(self, data):
        funcion = data.get("funcion")
        butaca = data.get("butaca")

        if self.instance is not None:
            funcion = funcion or self.instance.funcion
            butaca = butaca or self.instance.butaca

        if funcion and butaca and funcion.sala_id != butaca.sala_id:
            raise serializers.ValidationError(
                "La butaca seleccionada no pertenece a la sala de esta función."
            )
        return data