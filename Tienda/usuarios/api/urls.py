from django.urls import path
from usuarios.api.api import usuarios_api_view, usuario_api_view

urlpatterns = [
    #   .as_view() se usa para activar una clase
    # path ("usuarios/", UsuarioAPIView.as_view(), name = "usuario_api"),
    path ("usuarios/", usuarios_api_view, name = "usuarios_api"),
    path ("usuario/<int:id>/", usuario_api_view, name = "usuario_api_view")
]