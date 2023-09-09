from django.db import models
#   crear un modelo de usuario personalizado y PermissionsMixin agrega funcionalidad de permisos al usuario
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
#    prepara tu modelo de usuario personalizado para mantener un historial de los cambios realizados en las instancias de ese modelo
from simple_history.models import HistoricalRecords


class Gestor_Usuario(BaseUserManager):
    #   el guion bajo _ al prinsipio indica que el metodo e s privado y no debe ser accedido directamente desde fuera de la clase
    def _crear_usuario(self, usuario_nombre, email, nombre, apellido, contraseña, es_personal, es_superusuario, **campos_extra):
        usuario = self.model(
            usuario_nombre=usuario_nombre,
            email=email,
            nombre=nombre,
            apellido=apellido,
            es_personal=es_personal,
            es_superusuario=es_superusuario,
            #   es para agregar campos adisionales
            **campos_extra
        )
        #   set_password es para encriptar la contraseña
        usuario.set_password(contraseña)
        usuario.save(using=self.db)

        return usuario

    def crear_usuario(self, usuario_nombre, email, nombre, apellido, contraseña=None, **campos_extra):
        return self._crear_usuario(usuario_nombre, email, nombre, apellido, contraseña, False, False, **campos_extra)

    def crear_superusuario(self, usuario_nombre, email, nombre, apellido, contraseña=None, **campos_extra):
        return self._crear_usuario(usuario_nombre, email, nombre, apellido, contraseña, True, True, **campos_extra)

#   Este es el modelo de usuario personalizado.
class Usuario(AbstractBaseUser, PermissionsMixin):
    usuario_nombre = models.CharField(max_length=255, unique=True)
    #   cuando se coloca una etiqueta dentro del campo ('Correo Electrónico'), al crear un formulario abace del modelo el formulario muestra eso como nombre del campo
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True)
    nombre = models.CharField('Nombres', max_length=255, blank=True, null=True)
    apellido = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    imagen = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank=True)
    es_activo = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)
    #   registra el historial
    historico = HistoricalRecords()

    #   Esto afecta cómo se muestra el nombre del modelo en la interfaz de administración de Django.
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

#   Esta constante se utiliza para especificar cuál es el campo que se utilizará como nombre de usuario
CAMPO_USUARIO_NOMBRE = 'usuario_nombre'
#    contiene los nombres de los campos que se requieren cuando se crea un nuevo usuario como minimo
CAMPOS_REQUERIDOS = ['email', 'nombre', 'apellido']

def clave_natural(self):
    return self.usuario_nombre

def __str__(self):
    return f'{self.nombre} {self.apellido}'