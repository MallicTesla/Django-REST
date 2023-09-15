from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializers (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

#   asi se hace una serealizasion sin un modelo se construlle como si fuese un modelo
class TestUsuarioSerializers (serializers.Serializer):
    nombre = serializers.CharField(max_length=255)
    apellido = serializers.CharField(max_length=255)

#   cuando se valida este serealizador ejecuta estas funciones si no se encuentra la funcion con el nombre del campo pasa a la siguiente y por ultimo ejecuta (validate)
    def validate_nombre (self,value):
        print (f"validasion 1 {value}")
        return value

    def validate_apellido (self, value):
        print (f"validasion 2 {value}")
        return value

    def validate(self, value):
        print (f"validasion 3 {value}")
        return value



