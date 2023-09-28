# aca se definen las urls de los ViewSets
from rest_framework.routers import DefaultRouter
from productos.api.views.producsion_views import ProductoViewSets
from productos.api.views.general_views import UnidadeMedidaListaAPIView, CategoriaProductoListaAPIView, IndicadorListaAPIView

router = DefaultRouter()

#   asi se hacen las distintas rutas con viewset
#   primero colocas el nombre de la ruta y luego la clase del views despues podes nombrarla igual que las rutas en urls.py
router.register (r"productos", ProductoViewSets, basename = "prouctos")
router.register (r"unidad_medidas", UnidadeMedidaListaAPIView, basename = "unidad_medidas")
router.register (r"categorias", CategoriaProductoListaAPIView, basename = "categorias")
router.register (r"indicadores", IndicadorListaAPIView, basename = "indicadores")

urlpatterns = router.urls
