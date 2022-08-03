from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponseRedirect
from miapp.models import Producto
from miapp.models import Curso
from django.contrib import messages

# from .forms import CourseForm
# Create your views here.
layout = """"""
def inicio(request):
    return render(request, 'inicio.html')

def integrantes(request):
    integrantes = ['🧑 Jose Flores Chamba','🧑 Edson Alva Chanta','🧑 Miguel Motta Mendoza']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })


def crearcursos(request):
    return render(request, 'crear-curso.html')

def crearproductos(request):
    return render(request, 'crear-producto.html')

def formularioCurso(request):
    return render(request, 'curso-agregar.html')

def crear_producto(request):
    # RECIBE DATOS DEL FORMULARIO
    codigo = request.GET['codigo']
    nombre = request.GET['nombre']
    precio_compra = request.GET['precio_compra']
    precio_venta = request.GET['precio_venta']
    fecha_compra = request.GET['fecha_compra']
    estado = request.GET['estado']
    # CREAR OBJETO PRODUCTO
    producto = Producto(
        codigo = codigo,
        nombre = nombre,
        precio_venta = precio_venta,
        precio_compra = precio_compra,
        fecha_compra = fecha_compra,
        estado = estado
    )
    # GUARDA OBJETO
    producto.save()
    # MUESTRA MENSAJE FLASH
    messages.add_message(request, messages.SUCCESS, "Producto agregado con éxito")

    return redirect('/crearproductos/')

def crear_curso(request):
    # RECIBE DATOS DEL FORMULARIO
    codigo = request.GET['codigo']
    nombre = request.GET['nombre']
    horas = request.GET['horas']
    creditos = request.GET['creditos']
    estado = request.GET['estado']
    # CREAR OBJETO 
    curso = Curso(
        codigo = codigo,
        nombre = nombre,
        horas = horas,
        creditos = creditos,
        estado = estado
    )
    # GUARDA OBJETO
    curso.save()
    # MUESTRA MENSAJE FLASH
    messages.add_message(request, messages.SUCCESS, "Curso agregado con éxito")

    return redirect('/crearcursos/')

def productos(request):
    productos = Producto.objects.raw('SELECT * FROM miapp_producto')
    return render(request, 'productos.html', {'productos': productos})

def cursos(request):
    cursos = Curso.objects.raw('SELECT * FROM miapp_curso')
    return render(request, 'cursos.html', {'cursos': cursos})

def agregarCarrera(request):
    return render(request, 'carrera-agregar.html')




