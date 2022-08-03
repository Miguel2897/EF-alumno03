from django.db import models
from datetime import datetime
 
fechaHoy = datetime.now()

# Create your models here.
class Producto(models.Model):
    codigo = models.TextField(max_length=8)
    nombre = models.TextField()
    precio_compra = models.IntegerField()
    precio_venta = models.IntegerField()
    fecha_compra = models.DateField()
    fecha_registro = models.DateField(default=fechaHoy)
    estado = models.TextField(max_length=1, default='A')

class Curso(models.Model):
    codigo = models.TextField(max_length=8)
    nombre = models.TextField()
    horas = models.TextField()
    creditos = models.TextField()
    fecha_registro = models.DateField(default=fechaHoy)
    estado = models.TextField(max_length=1, default='A')
