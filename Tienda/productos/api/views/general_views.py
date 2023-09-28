from rest_framework import viewsets
from rest_framework import generics

from productos.models import UnidadMedida, CategoriaProducto, Indicador
from productos.api.serealizadores.general_serealaizer import UnidadMedidaSerealizera, CategoriaProductoSerealizera, IndicadorSerealizera
from base.api import GeneralListaApiView

# -----------------------------------------------------------------------------------------------------------------------------

#   asi se hace si queres ahorarte el get_queryset
#   tambien se puede usar GeneralListaApiView
class UnidadeMedidaListaAPIView (viewsets.ModelViewSet):
    serializer_class = UnidadMedidaSerealizera

class CategoriaProductoListaAPIView (viewsets.ModelViewSet):
    serializer_class = CategoriaProductoSerealizera

class IndicadorListaAPIView (viewsets.ModelViewSet):
    serializer_class = IndicadorSerealizera

# ----------------------------------------------------------------------------------------------------------------------------------

# class UnidadeMedidaListaAPIView (generics.ListAPIView):
#     serializer_class = UnidadMedidaSerealizera

#     def get_queryset(self):
#         return UnidadMedida.objects.filter (estado = True)

# class CategoriaProductoListaAPIView (generics.ListAPIView):
#     serializer_class = CategoriaProductoSerealizera

#     def get_queryset(self):
#         return CategoriaProducto.objects.filter (estado = True)

# class IndicadorListaAPIView (generics.ListAPIView):
#     serializer_class = IndicadorSerealizera

#     def get_queryset(self):
#         return Indicador.objects.filter (estado = True)


