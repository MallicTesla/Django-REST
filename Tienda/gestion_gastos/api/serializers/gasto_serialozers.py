from rest_framework import serializers

from gestion_gastos.models import Provedor

class GastoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Provedor
        exclude = ("id")

        