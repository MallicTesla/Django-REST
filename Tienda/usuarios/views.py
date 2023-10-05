from datetime import datetime

# esto controla las sesiones de django
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from usuarios.api.serializers import UsuarioTokenSerializers

class UsuarioToken (APIView):
    def get (self, request, *args, **kwargs):
        nombre_usuario = request.GET.get ("username")
        try:
            # trae el nombre del usuario a cual le pertenese el token
            usuario_token = Token.objects.get(user = UsuarioTokenSerializers().Meta.model.objects.filter(nombre_usuario = nombre_usuario).first())

            return Response ({"Token views": usuario_token.key})
        except KeyError as e:
            print (e)
            return Response ({"error views": "credensiales enviadas incorectas"}, status = status.HTTP_400_BAD_REQUEST)


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


class Logaut (APIView):
    # se puede hacer tambien con un metodo post
    def get (self, request, *args, **kwargs):
        try:
            # el token para el logaut tiene que venir desde el fron end en este caso en una variavle llamada token
            token = request.GET.get("token")
            print("token",token)
            token = Token.objects.filter(key = token).first()
            if token:
                usuario = token.user

                # esto es para cerar todas las sesiones abiertas si son del mismo usuario
                # toma todas las sesiones nuevas
                sesiones = Session.objects.filter(expire_date__gte = datetime.now())
                # comprueva si existen varias sesiones
                if sesiones.exists():
                    for sesion in sesiones :
                        sesion_data = sesion.get_decoded()

                        # comprueva si el id del usuario es igual al id de la sesion
                        if usuario.id == int (sesion_data.get ("_auth_user_id")):
                            # bora las sesiones aviertas
                            sesion.delete()

                token.delete()
                mensage_sesion = "Sesion de usuario eliminado."
                token_mensaje = "Token eliminado."

                return Response ({"token_mensaje":token_mensaje, "mensage_sesion": mensage_sesion}, status = status.HTTP_200_OK)
            return Response ({"error":"No se a encntrado ningun usuario con esas credensiales"}, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response ({"Error": "No se a encontrado ningun token en la peticion"}, status = status.HTTP_409_CONFLICT)





