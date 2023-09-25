# aca irian los serealizadores de los modelos que el usuario no interactua directamente
from productos.models import UnidadMedida, CategoriaProducto, Indicador
from rest_framework import serializers

class UnidadMedidaSerealizera (serializers.ModelSerializer):
    class Meta :
        model = UnidadMedida
        #   se esclulle el campo "state" que es un campo interno que se rellena de forma automatica
        exclude = ("estado",)

class CategoriaProductoSerealizera (serializers.ModelSerializer):
    class Meta :
        model = CategoriaProducto
        exclude = ("estado",)

class IndicadorSerealizera (serializers.ModelSerializer):
    class Meta :
        model = Indicador
        exclude = ("estado",)

