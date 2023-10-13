from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from usuarios.views import Login, Logaut
#   version para el fron
# from usuarios.views_fron import Login, Logaut, UsuarioToken
# from usuarios.views import Login, Logaut, UsuarioToken

#   JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        #   si modificas estos parametros se ven en la parte prinsipal de la app
        title="Documentacion de mi API",
        default_version='v0.1',
        description="Documentacion pubilca de mi API Tienda",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="El_mallic@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ...
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path ("usuario/", include("usuarios.api.urls")),
    # path ("productos/", include ("productos.api.urls")),
    path ("productos/", include ("productos.api.routers")),
    path("login/", Login.as_view(), name = "login"),
    path("logaut/", Logaut.as_view(), name="logaut"),
    #   con JWT no se necesita 
    # path("refrescar_token/", UsuarioToken.as_view(), name="refrescar_tokn"),

    #   JWT
    #   esta ruta sirve para retornar y refrescar el token de acseso para un usuario y contraseña que se le envia
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #   refresca el toquen que estas usando
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #   app SWAGGER
    re_path ('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path ('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path ('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
