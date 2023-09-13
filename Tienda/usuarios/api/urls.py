from django.urls import path
from usuarios.api.api import usuario_api_view

urlpatterns = [
    #   .as_view() se usa para activar una clase
    # path ("usuario/", UsuarioAPIView.as_view(), name = "usuario_api"),
    path ("usuario/", usuario_api_view, name = "usuario_api"),
]