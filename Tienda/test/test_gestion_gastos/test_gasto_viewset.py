# para buscar un provedor primero tenes que crear uno en fabrica
from rest_framework import status

from test.test_setup import TestSetUp
from test.fabrica.gestion_gastos.gasto_favrica import ProvedorFabrica

from gestion_gastos.models import Provedor

class GastoTestCase (TestSetUp):
    url_prinsipal = "/gasto/gastos/"

    #   buscar un provedor que si existe
    def test_buscar_provedor (self):
        #   primero se fabrica el provedor despues va la ruta con la que se busca el provedor
        provedor = ProvedorFabrica().crear_provedor()
        response = self.client.get (
            #   primero la ruta
            self.url_prinsipal + "buscar_provedor/",
            #   despues los parametros requeridos
            {"ruc_o_negosio" : provedor.ruc},
            format = "json"
        )

        #   comprueva si la respuesta http es la misma
        self.assertEqual (response.status_code, status.HTTP_200_OK)
        #   comprueva si el ruc que resivis es el mismo que le mandastes
        self.assertEqual (response.data["ruc"], provedor.ruc)

    #   buscar un provedor que no existe
    def test_busqueda_provedor_error (self):
        #   primero se fabrica el provedor despues va la ruta con la que se busca el provedor
        provedor = ProvedorFabrica().crear_provedor()
        response = self.client.get (
            #   primero la ruta
            self.url_prinsipal + "buscar_provedor/",
            #   despues los parametros requeridos
            {"ruc_o_negosio" : "cualquier ruc 32165465"},
            format = "json"
        )

        #   comprueva si la respuesta http es la misma
        self.assertEqual (response.status_code, status.HTTP_400_BAD_REQUEST)
        #   comprueva si el mensage que resivis es el mismo
        self.assertEqual (response.data["Mensage"], "No se a encontrado ningun provedor")


    def test_nuevo_provedor (self):
        provedor = ProvedorFabrica().construir_provedor_JSON()
        response = self.client.post (
            self.url_prinsipal + "nuevo_provedor/",
            provedor,
            format = "json",
        )

        self.assertEqual (response.status_code, status.HTTP_201_CREATED)
        self.assertEqual (Provedor.objects.all().count(), 1)
        self.assertEqual (response.data ["Provedor"] ["ruc"], provedor ["ruc"])