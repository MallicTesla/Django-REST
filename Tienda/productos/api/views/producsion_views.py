from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from base.api import GeneralListaApiView
from productos.api.serealizadores.producto_serealizador import ProductoSerealizera


class ProdctoListaAPIView (GeneralListaApiView):
    serializer_class = ProductoSerealizera

#   con CreateAPIView solo da un metodo PUT
class ProductoCrearAPIView (generics.CreateAPIView):
    serializer_class = ProductoSerealizera

    #   asi es para personalisar el mensage despues de hacer un PUT
    def post(self, request):
        serealizador = self.serializer_class (data = request.data)
        if serealizador.is_valid():
            serealizador.save()
            return Response ({"message":"Producto creado corectamente"}, status = status.HTTP_201_CREATED)
        return Response (serealizador.errors, status = status.HTTP_400_BAD_REQUEST)

#   devuelve un solo producto
class ProductoDevuelveAPIView (generics.RetrieveAPIView):
    serializer_class = ProductoSerealizera

    # muestra el producto
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = True)

#   asi borras un producto directamente de la base de datos no es muy recomendavle hacerlo
class ProductoBorrarAPIView (generics.DestroyAPIView):
    serializer_class = ProductoSerealizera

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = True)

    #   asi se relasa una eliminasion logica que cambia el estado de activo a inactivo
    def delete (self, request, pk = None):
        producto = self.get_queryset().filter(id = pk).first()
        if producto :
            producto.estado = False
            producto.save()
            return Response ({"message":"Eliminado corectamente"}, status = status.HTTP_200_OK)
        return Response ({"error":"No se encuentra ningun producto con esos datos"}, status = status.HTTP_400_BAD_REQUEST)

