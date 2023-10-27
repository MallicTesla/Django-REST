#   este archivo se usa para inisiar sesion para realisar los test
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker


class TestSetUp (APITestCase):
    def setUp (self):
        from usuarios.models import Usuario

        faker = Faker()
        #   la ruta con la que se inisia sesion
        self.login_url = "/login/" # tamvien puede ser (reverse)
        #   crea un super usuario con estos datos
        self.usuario = Usuario.objects.create_superuser(
            nombre_usuario = "Test_mallic",
            email = faker.email(),
            nombre = "Test_mallic",
            apellido = "Test_mallic",
            password = "123"
        )

        #   client simula ser un navegador se tiene que espesificar que metodo va a usar
        response = self.client.post(
            # primero va la ruta de login y despues los dtos para inisiar sesion
            self.login_url,
            {   "nombre_usuario": self.usuario.nombre_usuario,
                "password": "123"},
            format = "json"
        )

        #   verifica la ifualdad de dos valores separados por coma (,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #   aca guarda el token con el que inisiastes sesion
        self.token = response.data ["token"]
        #   aca se setea la instansia credentials con las credensiales con la que se envia las petisiones
        self.client.credentials(HTTP_AUTHORIZATION="BEARER" + self.token)
        #   aca se logea
        return super().setUp()


    # def test_guion_cualquier_cosa (self):
    #     print (self.token)
