from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from usuarios.autentificasion import ExpirasonTokenAuthentication

class Autentificador (object):
    # esto es para enviar al fron
    usuario = None
    #      nuevo
    # usuario_token_expirado = False

    def get_user (self, request):
        token = get_authorization_header(request).split()

        if token:
            try:
                token = token [1].decode()

            except:
                return None

            token_expirado = ExpirasonTokenAuthentication()
            #   nuevo
            # usuario, token, mensage, self.usuario_token_expirado  =  token_expirado.authenticate_credentials(token)
            usuario  =  token_expirado.authenticate_credentials(token)

            #   nuevo
            # if usuario != None and token != None:
            if usuario != None:
                self.usuario = usuario
                return usuario

            #   nuevo
            # return mensage

        return None

    # el metodo dispath es el primer metodo que llaman las clases en django
    def dispatch(self, request, *args, **kwargs):
        usuario = self.get_user(request)

        #   pasa esto si se encuentra un token
        if usuario is not None:
            # nuevo
            # if type(usuario) == str:

            #     response = Response ({"Error ": usuario, "expiro": self.usuario_token_expirado}, status = status.HTTP_401_UNAUTHORIZED)
            #     response.accepted_renderer = JSONRenderer()
            #     response.accepted_media_type = "application/json"
            #     response.renderer_context = {}
            #     return response

            # # asi se evitaque que cuando entras por primera ves con un token invalido muestre la info
            if not self.usuario_token_expirado:
                return super().dispatch(request, *args, **kwargs)
        
        # este error (.accepted_renderer not set on Response) es porque cuando creas una clase que no hereda de una clase de rest_framework
        # pide que le retornes un valor en formato json
        # response = Response (   {"Error dispatch :":"No se han enviado las credenciales", "expiro otro": self.usuario_token_expirado},status = status.HTTP_400_BAD_REQUEST)
        #   nuevo
        response = Response (   {"Error dispatch :":"No se han enviado las credenciales"},status = status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response