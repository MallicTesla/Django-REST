# aca se definen las urls de los ViewSets
from rest_framework.routers import DefaultRouter
from productos.api.views.producsion_views import ProductoViewSets

router = DefaultRouter()

#   primero colocas el nombre de la ruta y luego la clase del views despues podes nombrarla igual que las rutas en urls.py
router.register (r"productos", ProductoViewSets, basename = "prouctos")

urlpatterns = router.urls
