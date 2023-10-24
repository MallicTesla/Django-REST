from rest_framework import serializers

from gestion_gastos.models import Provedor

class ProvedorSerializer(serializers.ModelSerializer):
    class Meta :
        model = Provedor
        fields = ("id", "ruc", "negosio", "direcsion", )