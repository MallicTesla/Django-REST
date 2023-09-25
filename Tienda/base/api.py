from rest_framework import generics

# esto se usa para no repetir tanto codigo en general_views.py
class GeneralListaApiView (generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        #   get_serializer entras a al serealizador y luego entras a la clase meta y despues entras al atributo model
        model = self.get_serializer().Meta.model
        return model.objects.filter (estado = True)