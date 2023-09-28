from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("usuario/", include("usuarios.api.urls")),
    # path ("productos/", include ("productos.api.urls")),
    path ("productos/", include ("productos.api.routers")),
    
]
