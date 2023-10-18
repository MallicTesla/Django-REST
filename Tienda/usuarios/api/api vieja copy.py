# este archivo rempasa al views
from rest_framework.request import Request
from rest_framework.response import Response
#   muestra los codigos de estados la ducumentasion https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from usuarios.models import Usuario
from usuarios.api.serializers import UsuarioSerializers, TestUsuarioSerializers, UsuarioListaSerializaes


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
        #   .value (los campos que queres mostrar) tenes que agregar to_representation en el serealizador
        usuarios = Usuario.objects.all().values ("id", "nombre_usuario", "email", "password")
        #   cuando queres serealizar un listado tenes que agregarle (many = True) para que sepa que es mas de uno
        usuarios_serializer = UsuarioListaSerializaes (usuarios, many = True)

        # #   prueba creando todo el serealizador
        # tes_data = {
        #     "nombre":"nombre_api_view",
        #     "apellido":"apellido_api_view"
        # }
        # #   con (context = tes_data) le pasas el contexto al serializers 
        # tes_data = TestUsuarioSerializers(data = tes_data, context = tes_data)
        # print ("antes de validar")
        # if tes_data.is_valid():
        #     print ("quedo")
        #     Usuario_instance = tes_data.save()
        #     print (f"guardado {Usuario_instance}")
        # else:
        #     print (tes_data.errors)

        # para pasar el json se tiene que agregar (.data) al final de de la info serealizada
        return Response (usuarios_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "POST":
        usuarios_serializer = UsuarioSerializers (data = request.data)

        if usuarios_serializer.is_valid () :
            usuarios_serializer.save ()
            return Response (usuarios_serializer.data, status = status.HTTP_201_CREATED)

        return Response (usuarios_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view (["GET", "PUT", "DELETE"])
def usuario_api_view (request:Request, id):
    #   esto es igual que usar objects.get (id=id)
    usuario = Usuario.objects.filter(id = id ).first()

    if usuario:
        #   selecsiona a un usuario por id
        if request.method == "GET":

            usuario_seria = UsuarioSerializers (usuario)

            return Response (usuario_seria.data, status = status.HTTP_200_OK)

        #   para editar un usuario
        elif request.method == "PUT":
            #   la informasion de la actualisasion se guarda en (data=request.data)
            usuario_seria = UsuarioSerializers(usuario, data=request.data)

            #   cuando actualis un modelo por medio de un serealizador personalisado
            #   el context = request.data es encaso que las otras validadores rquieran una validasion anterior 
            # usuario_seria = TestUsuarioSerializers (usuario, data=request.data, context = request.data)

            if usuario_seria.is_valid():
                usuario_seria.save()

                return Response(usuario_seria.data, status = status.HTTP_200_OK)

            return Response(usuario_seria.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            usuario.delete()

            return Response ({"message":"Usuario elimonado corectamente"}, status = status.HTTP_200_OK)
        
    return Response ({"message":"No se encontro ninguna coinsidensia"}, status = status.HTTP_400_BAD_REQUEST)


