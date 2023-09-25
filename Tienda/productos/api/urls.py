from django.urls import path
from productos.api.views.general_views import UnidadeMedidaListaAPIView, CategoriaProductoListaAPIView, IndicadorListaAPIView

urlpatterns = [
    #   asi se hace la view cuando usas una clase
    path ("unidad_medida/", UnidadeMedidaListaAPIView.as_view(), name = "unidad_medida"),
    path ("categoria_producto/", CategoriaProductoListaAPIView.as_view(), name = "categoria_producto"),
    path ("indicador/", IndicadorListaAPIView.as_view(), name = "indicador"),
]