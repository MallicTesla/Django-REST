from django.urls import path
from productos.api.views.general_views import UnidadeMedidaListaAPIView, CategoriaProductoListaAPIView, IndicadorListaAPIView
from productos.api.views.producsion_views import ProdctoListaAPIView

urlpatterns = [
    #   asi se hace la view cuando usas una clase
    path ("unidad_medida/", UnidadeMedidaListaAPIView.as_view(), name = "unidad_medida"),
    path ("categoria_producto/", CategoriaProductoListaAPIView.as_view(), name = "categoria_producto"),
    path ("indicador/", IndicadorListaAPIView.as_view(), name = "indicador"),
    path ("productos/", ProdctoListaAPIView.as_view(), name = "Productos")
]