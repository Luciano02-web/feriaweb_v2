from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class Jean(models.Model):
    def __str__(self):
        return f'Jean: {self.id_vuelo} ----- sale el: {self.fecha}'
    id_vuelo = models.IntegerField()
    salida = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    fecha = models.DateField()    #2022-05-23(AAAA-MM-DD)
    hora_de_salida = models.TimeField() #02:13(HH:MM)
"""


OPCIONESGENERO=[
    ('Hombre','Hombre'),('Mujer','Mujer')
]



class Jean(models.Model):
    def __str__(self):
        return f'Jean: {self.codigo} ----- Talle: {self.talle} ----- Color: {self.color} ----- Precio: {self.precio} ----- Genero: {self.genero}'
    codigo = models.IntegerField(unique=True)
    talle = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField()
    genero = models.CharField(max_length=50, choices=OPCIONESGENERO,default='Mujer')
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)#blank=True
    imagen_b = models.ImageField(upload_to="avatares", null=True, blank=True)


class Remera(models.Model):
    def __str__(self):
        return f'Remera: {self.codigo} ----- Talle: {self.talle} ----- Color: {self.color} ----- Precio: {self.precio} ----- Genero: {self.genero}'
    codigo = models.IntegerField(unique=True)
    talle = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField()
    genero = models.CharField(max_length=50, choices=OPCIONESGENERO,default='Mujer')
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    imagen_b = models.ImageField(upload_to="avatares", null=True, blank=True)

class Camisa(models.Model):
    def __str__(self):
        return f'Camisa: {self.codigo} ----- Talle: {self.talle} ----- Color: {self.color} ----- Precio: {self.precio} ----- Genero: {self.genero}'
    codigo = models.IntegerField(unique=True)
    talle = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField()
    genero = models.CharField(max_length=50, choices=OPCIONESGENERO,default='Mujer')
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)#blank=True
    imagen_b = models.ImageField(upload_to="avatares", null=True, blank=True)



class Campera(models.Model):
    def __str__(self):
        return f'Campera: {self.codigo} ----- Talle: {self.talle} ----- Color: {self.color} ----- Precio: {self.precio} ----- Genero: {self.genero}'
    codigo = models.IntegerField(unique=True)
    talle = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField()
    genero = models.CharField(max_length=50, choices=OPCIONESGENERO,default='Mujer')
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)#blank=True
    imagen_b = models.ImageField(upload_to="avatares", null=True, blank=True)

class Todo100(models.Model):
    def __str__(self):
        return f'Todo $100: {self.codigo} ----- Talle: {self.talle} ----- Color: {self.color} ----- Precio: {self.precio} ----- Genero: {self.genero}'
    codigo = models.IntegerField(unique=True)
    talle = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField()
    genero = models.CharField(max_length=50, choices=OPCIONESGENERO,default='Mujer')
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)#blank=True
    imagen_b = models.ImageField(upload_to="avatares", null=True, blank=True)

class Calzado(models.Model):
    def __str__(self):
        return f'Calzado: {self.codigo} ----- Talle: {self.talle} ----- Color: {self.color} ----- Precio: {self.precio} ----- Genero: {self.genero}'
    codigo = models.IntegerField(unique=True)
    talle = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField()
    genero = models.CharField(max_length=50, choices=OPCIONESGENERO,default='Mujer')
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)#blank=True
    imagen_b = models.ImageField(upload_to="avatares", null=True, blank=True)

class Invernal(models.Model):
    def __str__(self):
        return f'Invernal: {self.codigo} ----- Talle: {self.talle} ----- Color: {self.color} ----- Precio: {self.precio} ----- Genero: {self.genero}'
    codigo = models.IntegerField(unique=True)
    talle = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField()
    genero = models.CharField(max_length=50, choices=OPCIONESGENERO,default='Mujer')
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)#blank=True
    imagen_b = models.ImageField(upload_to="avatares", null=True, blank=True)

class Pantalon(models.Model):
    def __str__(self):
        return f'Pantalon: {self.codigo} ----- Talle: {self.talle} ----- Color: {self.color} ----- Precio: {self.precio} ----- Genero: {self.genero}'
    codigo = models.IntegerField(unique=True)
    talle = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    precio = models.IntegerField()
    genero = models.CharField(max_length=50, choices=OPCIONESGENERO,default='Mujer')
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)#blank=True
    imagen_b = models.ImageField(upload_to="avatares", null=True, blank=True)
"""
class Avatar(models.Model):
    def __str__(self):
        return f'Avatar: {self.usuario}' 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
"""
class Imagen(models.Model):
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    imagen_b = models.ImageField(upload_to="avatares_B", null=True, blank=True)

#class Imagen_b(models.Model):
#    imagen_b = models.ImageField(upload_to="avatares_B", null=True, blank=True)