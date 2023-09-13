from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializers (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"