from base.api import GeneralListaApiView
from productos.api.serealizadores.producto_serealizador import ProductoSerealizera


class ProdctoListaAPIView (GeneralListaApiView):
    serializer_class = ProductoSerealizera