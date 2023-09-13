# este archivo rempasa al views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from usuarios.models import Usuario
from usuarios.api.serializers import UsuarioSerializers


# class UsuarioAPIView (APIView):
#     def get (self,request):
#         usuarios=Usuario.objects.all ()
#         #   cuando queres serealizar un listado tenes que agregarle (many = True) para que sepa que es mas de uno
#         usuarios_serializer = UsuarioSerializers (usuarios, many = True)

#         # para pasar el json se tiene que agregar (.data) al final de de la info serealizada
#         return Response (usuarios_serializer.data)

#   esto hace lo mismo que la clase UsuarioAPIView
#   al decorador se le pasa que metodos se le van a permiter que tenga la funcion
@api_view (["GET","POST"])
def usuario_api_view (request):
    if request.method == "GET":
        usuarios=Usuario.objects.all ()
        #   cuando queres serealizar un listado tenes que agregarle (many = True) para que sepa que es mas de uno
        usuarios_serializer = UsuarioSerializers (usuarios, many = True)

        # para pasar el json se tiene que agregar (.data) al final de de la info serealizada
        return Response (usuarios_serializer.data)
    
    elif request.method == "POST":
        usuarios_serializer = UsuarioSerializers (data = request.data)

        if usuarios_serializer.is_valid () :
            usuarios_serializer.save ()
            return Response (usuarios_serializer.data)
        
        return Response (usuarios_serializer.errors)