from datetime import datetime

# esto controla las sesiones de django
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from usuarios.api.serializers import UsuarioTokenSerializers


class Login (ObtainAuthToken):
    def post (self,request, *args, **kwargs):
        print (request.user)
        #   optiene un usuario
        login_serializer = self.serializer_class (data = request.data, context = {"request":request})
        print (login_serializer)
        #   verifica si el usuario esta en la base de datos
        if login_serializer.is_valid():
            usuario = login_serializer.validated_data["user"]

            if usuario.is_active:
                #   esto debelve dos balores por eso la coma,
                token,created = Token.objects.get_or_create (user = usuario)
                print (f"tokeen -- {token} \n created-- {created} ")
                usuario_serialaizer = UsuarioTokenSerializers (usuario)

                #   verifica si tiiene un toquen si lo tiene es True
                if created:
                    return Response ({  "token": token.key,
                                        "usuario": usuario_serialaizer.data,
                                        "mensage": "Inisio de sesion exitosa"},
                                        status = status.HTTP_200_OK)

                else:
                    # esto es para cerar todas las sesiones abiertas si son del mismo usuario
                    # # toma todas las sesiones nuevas
                    # sesiones = Session.objects.filter(expire_date__gte = datetime.now())
                    # # comprueva si existen varias sesiones
                    # if sesiones.exists():
                    #     for sesion in sesiones :
                    #         sesion_data = sesion.get_decoded()

                    #         # comprueva si el id del usuario es igual al id de la sesion
                    #         if usuario.id == int (sesion_data.get ("_auth_user_id")):
                    #             # bora las sesiones aviertas
                    #             sesion.delete()

                    # #   si tiene un token ya creado lo elimina y le crea uno nuevo
                    # token.delete()
                    # token = Token.objects.create (user = usuario)

                    # return Response ({  
                    #                     "token": token.key,
                    #                     "user": usuario_serialaizer.data,
                    #                     "mensage": "Inisio de sesion exitosa"},
                    #                     status = status.HTTP_200_OK)

                    # para bloquear que un usuario inisie sesion cuando ya esta inisiado
                    token.delete()
                    return Response ({"error":"ya as inisiado sesion con este usuario"}, status = status.HTTP_409_CONFLICT)

            else:
                return Response ({"error":"Este usuario no inisiar sesion"}, status = status.HTTP_401_UNAUTHORIZED)

        else:
            return Response ({"error":"nombre de usuario o contraseña incorecta"}, status = status.HTTP_400_BAD_REQUEST)

        return Response ({"mensaje":"funciono"}, status = status.HTTP_200_OK)