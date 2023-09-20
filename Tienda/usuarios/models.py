from django.db import models
#   crear un modelo de usuario personalizado y PermissionsMixin agrega funcionalidad de permisos al usuario
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
#    prepara tu modelo de usuario personalizado para mantener un historial de los cambios realizados en las instancias de ese modelo
from simple_history.models import HistoricalRecords

class Gestor_Usuario(BaseUserManager):
    #   el guion bajo _ al prinsipio indica que el metodo es privado y no debe ser accedido directamente desde fuera de la clase
    def _crear_usuario(self, nombre_usuario, email, nombre, apellido, password, is_staff , is_superuser, **extra_fields):
        usuario = self.model(
            nombre_usuario=nombre_usuario,
            email=email,
            nombre=nombre,
            apellido=apellido,
            is_staff =is_staff ,
            is_superuser=is_superuser,
            #   es para agregar campos adisionales
            **extra_fields
        )
        #   set_password es para encriptar la password
        usuario.set_password(password)
        usuario.save(using=self.db)

        return usuario

    #   es para buscar un usuario por su nombre_usuario
    def get_by_natural_key(self, nombre_usuario):
        return self.get(nombre_usuario = nombre_usuario)

    def create_user(self, nombre_usuario, email, nombre, apellido, password=None, **extra_fields):
        return self._crear_usuario(nombre_usuario, email, nombre, apellido, password, False, False, **extra_fields)

    def create_superuser(self, nombre_usuario, email, nombre, apellido, password=None, **extra_fields):
        return self._crear_usuario(nombre_usuario, email, nombre, apellido, password, True, True, **extra_fields)

#   Este es el modelo de usuario personalizado.
class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre_usuario = models.CharField(max_length=255, unique=True)
    #   cuando se coloca una etiqueta dentro del campo ('Correo Electrónico'), al crear un formulario abace del modelo el formulario muestra eso como nombre del campo
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True)
    nombre = models.CharField('Nombres', max_length=255, blank=True, null=True)
    apellido = models.CharField('Apellido', max_length=255, blank=True, null=True)
    imagen = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank=True)
    es_activo = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)
    #   registra el historial
    historico = HistoricalRecords()

    objects = Gestor_Usuario()

    #   Esto afecta cómo se muestra el nombre del modelo en la interfaz de administración de Django.
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    #   Esta constante se utiliza para especificar cuál es el campo que se utilizará como nombre de usuario
    USERNAME_FIELD = 'nombre_usuario'
    #    contiene los nombres de los campos que se requieren cuando se crea un nuevo usuario como minimo
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    def natural_key (self):
        return (self.nombre_usuario,)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    #   este save es llamad desde el serealizador si no esta difinido usa el save por defecto del modelo
    # def save (self, *args, **kwargs):
    #     print ("estoy en el save del modelo")