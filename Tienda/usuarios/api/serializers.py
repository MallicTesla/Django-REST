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
#   estos son validasiones personalizadas
    def validate_nombre (self,value):
        print ("nombre")
        if "nombre_api_vie" == value:
            print (f"nombre if {value}")
            raise serializers.ValidationError("Error, el nombre no puede ser ese")
        return value

    def validate_apellido (self, value):
        if "" == value:
            raise serializers.ValidationError("Error, el coreo deve de estar completo")

        #   el contexto contiene una lista con toos los campos
        print (self.context)
        # if self.context["nombre"] in value :
        #   asi se te aseguras que el otro campo tamvien este vlalidado
        if self.validate_nombre(self.context["nombre"]) in value :
            print (f"apellido {value}")
            raise serializers.ValidationError("Error, el apellido no puede ser igual al nombre")

        return value

# despues de validar los campos anteriores si los pasa sigue con este validate
    def validate (self, data):
        # if data ['nombre'] in data ['apellido']:
        #     raise serializers.ValidationError("Error, el nombre y el apellido no puede ser el mismo")
        return data

    #   en esta clase se hace referensia a al modelo donde se tiene que guardar este serealisador seria el model de la clase Meta
    def create (self, validated_data):
        print (f"funcion create {validated_data}")
        #   lo que se guarda en el modelo serian vlidated_data
        return Usuario.objects.create (**validated_data)



