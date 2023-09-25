from productos.models import Producto
from rest_framework import serializers

class ProductoSerealizera (serializers.ModelSerializer):
    class Meta :
        model = Producto
        exclude = ("state",)