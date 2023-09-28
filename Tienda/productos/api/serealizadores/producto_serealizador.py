from rest_framework import serializers
from productos.models import Producto
from productos.api.serealizadores.general_serealaizer import UnidadMedidaSerealizera, CategoriaProductoSerealizera, IndicadorSerealizera

class ProductoSerealizera (serializers.ModelSerializer):
    # esta es una forma de mostrar el titulo de la relasion que tiene muestra todo lo espesificaddo en el serealizador
    #   para que los campos muestren el nombre de la relasion
    #   primero va el campo de la relason y luego va el serealisador del modelo relasionado
    # unidad_medida = UnidadMedidaSerealizera()
    # categoria_producto = CategoriaProductoSerealizera()

    # asi muestra el str del modelo relasionado
    #   para que los campos muestren el nombre de la relasion
    #   primero va el campo de la relason 
    # unidad_medida = serializers.StringRelatedField()
    # categoria_producto = serializers.StringRelatedField()

    class Meta :
        model = Producto
        exclude = ("estado",)

    #  asi mostras el contenido de todos los campos inclillendo las relasinados
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "producto": instance.producto,
            "descripción_producto": instance.descripción_producto,
            #   cuando no tenes una imagen devuelve una cadena vasio y da error asi lo areglas
            "imagen_producto": instance.imagen_producto if instance.imagen_producto != "" else "",
            "unidad_medida": instance.unidad_medida.descripción if instance.unidad_medida is not None else "",
            "categoria_producto": instance.categoria_producto.descripción if instance.categoria_producto is not None else "",
        }