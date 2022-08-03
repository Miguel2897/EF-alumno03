
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', views.inicio, name = "inicio"),
    path('integrantes/', views.integrantes, name = "integrantes"),
    path('crearproductos/', views.crearproductos, name = "crearproductos"),
    path('crearcursos/', views.crearcursos, name = "crearcursos"),
    path('recibirproducto/', views.crear_producto, name = "recibirproducto"),
    path('recibircurso/', views.crear_curso, name = "recibircurso"),
    path('cursos/', views.cursos, name = "cursos"),
    path('productos/', views.productos , name = "productos"),
]
