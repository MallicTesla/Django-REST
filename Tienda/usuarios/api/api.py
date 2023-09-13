# este archivo rempasa al views
from rest_framework.response import Response
from rest_framework.views import APIView
from usuarios.models import Usuario
from usuarios.api.serializers import UsuarioSerializers

class UsuarioAPIView (APIView):
    def get (self,request):
        usuarios=Usuario.objects.all ()
        #   cuando queres serealizar un listado tenes que agregarle (many = True) para que sepa que es mas de uno
        usuarios_serializer = UsuarioSerializers (usuarios, many = True)

        # para pasar el jeison se tiene que agregar (.data) al final de de la info serealizada
        return Response (usuarios_serializer.data)