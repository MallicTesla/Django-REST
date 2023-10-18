from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework. response import Response
from rest_framework.decorators import api_view

from usuarios.models import Usuario
from usuarios.api.serializers import UsuarioSerializers, UsuarioListaSerializaes


#   GenericViewSet no automatisa ningun metodo pero si los permite
class UsuarioViwSet (viewsets.GenericViewSet):
    serializer_class = UsuarioSerializers
    list_serializer_class = UsuarioListaSerializaes
    #   GenericViewSet viene con esta variable en none por defecto asi que no es nesesaria aserlo aca
    queryset = None

    def get_queryset(self):
        if self.queryset is not None:
            # optiene todos los usuarios con el atributo is_active = True
            self.queryset = self.serializer_class().Meta.model.objects.filter (is_active = True)
        return self.queryset


    def list (self, request:Request):
        pass






