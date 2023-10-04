from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from usuarios.autentificasion import ExpirasonTokenAuthentication

class Autentificador (object):
    def get_user (self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token [1].decode()

            except:
                return None

            token_expirado = ExpirasonTokenAuthentication()
            usuario, token, mensage  =  token_expirado.authenticate_credentials(token)

            if usuario != None and token != None:
                return usuario

            return mensage

        return None

    # el metodo dispath es el primer metodo que llaman las clases en django
    def dispatch(self, request, *args, **kwargs):
        usuario = self.get_user(request)

        #   pasa esto si se encuentra un token
        if usuario is not None:
            if type(usuario) == str:

                response = Response ({"Error ": usuario})
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                return response
            return super().dispatch(request, *args, **kwargs)
        
        # este error (.accepted_renderer not set on Response) es porque cuando creas una clase que no hereda de una clase de rest_framework
        # pide que le retornes un valor en formato json
        response = Response ({"Error dispatch :":"No se han enviado las credenciales"})
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response