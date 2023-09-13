from django.urls import path
from usuarios.api.api import UsuarioAPIView

urlpatterns = [
    path ("usuario/", UsuarioAPIView.as_view(), name = "usuario_api")
]