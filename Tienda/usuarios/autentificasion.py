from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


#   es para añadirle tiempo de expirasion a los token
class ExpirasonTokenAuthentication (TokenAuthentication):
    def 
    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related("user").get (key = key)

        except self.get_model().DoesNotExist:
            raise AuthenticationFailed ("Token invalido.")

        if not token.user.is_active:
            raise AuthenticationFailed ("Uauario no activo o eliminado")
        
        is_expired = token_expire_handler (token)
    