#   cuando se usa GenericViewSet enves de urls se usa routers
from rest_framework.routers import DefaultRouter

from usuarios.api.api import UsuarioViwSet

router = DefaultRouter()

router.register ("usuarios", UsuarioViwSet, basename = "usuario")

urlpatterns = router.urls



