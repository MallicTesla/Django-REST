from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializers (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def create(self, validated_data):
        usuario = Usuario (**validated_data)
        #   aca se toma la contraseña cuando creas un usuario nuevo y la encripta
        usuario.set_password (validated_data ["password"])
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        #   aca encripta la contraseña al actualisar un usuario
        usuario = super().update(instance, validated_data)
        usuario.set_password (validated_data ["password"])
        usuario.save()
        return usuario


#   esta clase se usa para ver la todos los usuarios y algunos de sus campos
class UsuarioListaSerializaes (serializers.ModelSerializer):
    class Meta :
        model = Usuario

    def to_representation (self, instance):
        print (f"desde serealizador f {instance}")
        #   asi se llama a la automatizasion del serealizador para que funsione normal mente
        # super().to_representation (instance)
        #   asi muestra solo los campos definidos tambien se tienen que definir en el objeto en api.py
        #   si se usa .values en el objeto en api.py aca se tiene que pasar los campos como si fuera una lista sino se le pasa solo el atributo id":instance.id,
        return {
            #   podes modificar lo que esta antes del instance para que muestre eso sin modificar el modelo
            "id":instance ["id"],
            "nombre de usuario":instance ["nombre_usuario"],
            "correo":instance ["email"],
            "password":instance ["password"]
        }


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

    #   cuando queres actualisar llama a esta funcion
    #   si en los otros validadores se vlida un campo anterior en la funcion de actualizar (PUT) se le tiene que pasar (context = request.data)
    def update (self, instance, validated_data):
        print (f"actializado")
        #   primero va el nombre del campo en la lista y despues va el campo del modelo
        instance.nombre = validated_data.get ("nombre", instance.nombre)
        instance.apellido = validated_data.get ("apellido", instance.apellido)
        #   este metodo save() guarda directamente sobre el modelo que tambien se puede crear un funsion save para que realise otra operacion
        instance.save()
        return instance

    #   con esta funsion podes elegir donde guardarlo o que realise otra operasion al momento de gardarse
    #   este save se llama desde api.py 
    # def save (self):
    #     print (self.validated_data)
