from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.listar, name="listar"),
    path(r'crear', views.crear, name="crear"),
    path(r'editar/<int:id>', views.editar, name="editar"),
    path(r'detalles/<int:id>', views.detalles, name="detalles"),
    path(r'eliminar/<int:id>', views.eliminar, name="eliminar"),
    path(r'publicaciones/', views.publicaciones, name="publicaciones"),
    path(r'muro/listar/publicaciones/', views.listarPublicaciones, name="listar-publicaciones"),
    path(r'muro/filtrar/fecha/', views.filtrarPorFecha, name="filtrar-por-Fecha"),
    re_path(r'muro/filtrar/busqueda/(?P<query>\w+)', views.filtrarPorBusqueda, name="filtrar-por-busqueda"),
    path(r'muro/detalle/publicacion/<int:id>', views.detallePublicacion, name="detalle-publicacion")
]