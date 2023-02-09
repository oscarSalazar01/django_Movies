from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.TextField()
    calificacion = models.IntegerField()
    pais = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} - {self.titulo}, {self.calificacion}, {self.pais}"

class Pelicula_location(models.Model):
    titulo = models.TextField()
    calificacion = models.IntegerField()
    pais = models.CharField(max_length=200)
    point = models.PointField()

    def __str__(self):
        return f"{self.id} - {self.titulo}, {self.calificacion}, {self.pais}, {self.point}"



