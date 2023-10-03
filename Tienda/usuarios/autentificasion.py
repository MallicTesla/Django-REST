from datetime import timedelta

from django.utils import timezone 
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


#   es para añadirle tiempo de expirasion a los token
class ExpirasonTokenAuthentication (TokenAuthentication):
    def expira_en (self,token):
        # se define el tiempo que a pasodo
        tiempo_pasado = timezone.now() - token.creted
        tiempo_restante = timedelta (seconds = settings.TIEMPO_EXPIRASION_TOKEN) - tiempo_pasado
        return tiempo_restante

    def token_expira_en (self,token):
        # compara la fecha de expirasion del token con la hora actual
        return self.expira_en (token) < timedelta (seconds = 0) 

    def si_expiro_token (self,token):
        si_expiro = self.token_expira_en (token)
        if si_expiro:
            print ("Token expirado")
        
        return si_expiro

    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related("user").get (key = key)

        except self.get_model().DoesNotExist:
            raise AuthenticationFailed ("Token invalido.")

        if not token.user.is_active:
            raise AuthenticationFailed ("Uauario no activo o eliminado")

        expiro = self.si_expiro_token (token)
        if expiro:
            return AuthenticationFailed ("Su token expiro")
        
        return (token.user.token)
    