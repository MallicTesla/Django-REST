#   para realisar un test de la ruta buscar_provedor primero se crrea un provedor
from gestion_gastos.models import Provedor

from faker import Faker

faker = Faker()

class ProvedorFabrica:

    def construir_provedor_JSON (self):
        return {
            "ruc" : str(faker.random_number(digits = 11)),
            "negosio" : faker.company(),
            "direcsion" : faker.address(),
            "telefono" : str (faker.random_number(digits=11)),
            "email" :   faker.email()
        }

    def crear_provedor (self):
        return Provedor.objects.create(**self.construir_provedor_JSON())