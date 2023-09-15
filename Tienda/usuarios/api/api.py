# este archivo rempasa al views
from rest_framework.request import Request
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
#   al decorador se le pasa los metodos que van a ser usados por la funcion
@api_view (["GET","POST"])
def usuarios_api_view (request:Request):
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

@api_view (["GET", "PUT", "DELETE"])
def usuario_api_view (request:Request, id):
    #   selecsiona a un usuario por id
    if request.method == "GET":
        #   esto es igual que usar objects.get (id=id)
        usuario = Usuario.objects.filter(id = id ).first()
        usuario_seria = UsuarioSerializers (usuario)

        return Response (usuario_seria.data)

    #   para editar un usuario
    elif request.method == "PUT":
        usuario = Usuario.objects.filter(id = id ).first()
        #   la informasion de la actualisasion se guarda en (data=request.data)
        usuario_seria = UsuarioSerializers(usuario, data=request.data)

        if usuario_seria.is_valid():
            usuario_seria.save()

            return Response(usuario_seria.data)

        return Response(usuario_seria.errors)
    
    elif request.method == "DELETE":
        usuario = Usuario.objects.filter(id = id ).first()
        usuario.delete()

        return Response ("Eliminado")


