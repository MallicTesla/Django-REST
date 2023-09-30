from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from usuarios.api.serializers import UsuarioListaSerializaes


class Login (ObtainAuthToken):
    def post (self,request, *args, **kwargs):
        print (request.user)
        #   optiene un usuario
        login_serializer = self.serializer_class (data = request.data, context = {"request":request})
        print (login_serializer)
        #   verifica si el usuario esta en la base de datos
        if login_serializer.is_valid():
            print ("1")
            usuario = login_serializer.validated_data["user"]

            if usuario.is_active:
                print ("2")
                #   esto debelve dos balores por eso la coma,
                token,created = Token.objects.get_or_create (user = usuario)
                print (f"tokeen -- {token} \n created-- {created} ")
                usuario_serialaizer = UsuarioListaSerializaes (usuario)
                print ("2.2")

                #   verifica si tiiene un toquen si lo tiene es True
                if created:
                    print ("3")
                    return Response ({  "token": token.key,
                                        "usuario": usuario_serialaizer.data,
                                        "mensage": "Inisio de sesion exitosa"},
                                        status = status.HTTP_200_OK)

                else:
                    #   si tiene un token ya creado lo elimina y le crea uno nuevo
                    print ("3.1")
                    token.delete()
                    token = Token.objects.create (user = usuario)
                    print ("3.2")
                    return Response ({  
                                        "token": token.key,
                                        "user": usuario_serialaizer.data,
                                        "mensage": "Inisio de sesion exitosa"},
                                        status = status.HTTP_200_OK)

            else:
                print ("4")
                return Response ({"error":"Este usuario no inisiar sesion"}, status = status.HTTP_401_UNAUTHORIZED)

        else:
            print ("5")
            return Response ({"error":"nombre de usuario o contraseña incorecta"}, status = status.HTTP_400_BAD_REQUEST)

        print ("6")
        return Response ({"mensaje":"funciono"}, status = status.HTTP_200_OK)