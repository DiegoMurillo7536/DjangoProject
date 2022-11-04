from tabnanny import verbose
from django.db import models

#crear modelo 

        
"""
class Product(models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    price = models.PositiveIntegerField(verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca')

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']
"""

class Team(models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre',null=False)
    flag = models.ImageField(verbose_name='Bandera',null=True,blank=True,upload_to='static/img')
    shield = models.ImageField(verbose_name='Escudo',null=True,blank=True,upload_to='static/img')

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'equipos'
        ordering = ['id']

class GamePosition(models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre',null=False)
    description = models.TextField(verbose_name='Descripción',null=False)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Posición'
        verbose_name_plural = 'Posiciones'
        db_table = 'posiciones'
        ordering = ['id']

class Coach(models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre',null=False)
    lastname = models.CharField(max_length=100,verbose_name='Apellido',null=True,blank=True)
    datebirth= models.DateField(verbose_name='Nacimiento',null=False)
    nation = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Nacionalidad')
    
    class Role(models.TextChoices):
        TECNICO = 'Técnico'
        ASISTENTE = 'Asistente'
        MEDICO = 'Médico'
        PREPARADOR = 'Preparador'
    
    role=models.CharField(max_length=20,choices=Role.choices, default=Role.TECNICO,)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        db_table = 'tecnicos'
        ordering = ['id']

class Player(models.Model):
    name = models.CharField (max_length=100, verbose_name='Nombre',null=False)
    lastname = models.CharField(max_length=100,verbose_name='Apellido',null=False)
    photo = models.ImageField(verbose_name='Foto',null=True,blank=True,upload_to='static/img')
    datebirth = models.DateField(verbose_name='Nacimiento',null=False)
    position= models.ManyToManyField(GamePosition,verbose_name='Posición',null=False)
    number = models.SmallIntegerField(verbose_name='Número',null=False)
    headline = models.BooleanField(verbose_name='Titular',null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Equipo')

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        db_table = 'jugadores'
        ordering = ['id']