#   modelo importado de otra app
from base.models import BaseModel

from django.db import models
# from simple_history.models import HistoricalRecords

class UnidadMedida (BaseModel):
    descripción = models.CharField ("Descripción", max_length = 50, blank = False, null = False, unique = True)
    # esto es para manegr los usuarios
    # historial = HistoricalRecords ()

    #  este decorador se utiliza para definir un método como una propiedad de solo lectura
    #  con esta funcion se opstiene el usuario que realiso la modificasion
    # @property
    # def _history_user (self):
    #     return self.changed_by
    
    #   con esta funcion se guarda el usuario que realiso la modificasion en el historial
    # @_history_user.setter
    # def _history_user (self, value):
    #     self.changed_by = value

    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidads de Medidas'

    def __str__(self):
        return self.descripción


class CategoriaProducto (BaseModel):
    descripción = models.CharField ("Descripción", max_length = 50, blank = False, null = False, unique = True)
    # historial = HistoricalRecords ()

    # @property
    # def _history_user (self):
    #     return self.changed_by
    
    # @_history_user.setter
    # def _history_user (self, value):
    #     self.changed_by = value

    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        return self.descripción


class Indicador (BaseModel):
    valor_descuento = models.PositiveSmallIntegerField (default = 0)
    categoria_producto = models.ForeignKey (UnidadMedida, on_delete = models.CASCADE, verbose_name = "Indicador de Oferta")
    # historial = HistoricalRecords ()

    # @property
    # def _history_user (self):
    #     return self.changed_by
    
    # @_history_user.setter
    # def _history_user (self, value):
    #     self.changed_by = value

    class Meta:
        verbose_name = 'Indicaor de Oferta'
        verbose_name_plural = 'Indicador de Ofertas'

    def __str__(self):
        return f"Oferta en la categoria {self.categoria_producto} : {self.valor_descuento}%"


class Producto (BaseModel):
    producto = models.CharField ("Producto", max_length = 150, unique = True, blank = False, null = False)
    descripción_producto = models.TextField ("Descripción del producto", null = False, unique = True)
    imagen_producto = models.ImageField("Imagen del producto", upload_to="productos_imagen/", blank = True, null = True)
    unidad_medida = models.ForeignKey (UnidadMedida, on_delete = models.CASCADE, verbose_name = "Unidad de medida", null = True)
    categoria_producto = models.ForeignKey (CategoriaProducto,on_delete = models.CASCADE, verbose_name = "Categoria del producto", null = True)
    # historial = HistoricalRecords ()

    # @property
    # def _history_user (self):
    #     return self.changed_by
    
    # @_history_user.setter
    # def _history_user (self, value):
    #     self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.producto

