from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.usuarios, name="usuarios"),
    path(r'desativar/<int:id>', views.desactivarUsuarios, name="perfil-desactivar"),
    path(r'autor/<int:id>', views.perfilAutor, name="perfil"),
    path(r'autor/editar/<int:id>', views.perfilEditar, name="perfil-editar"),
]