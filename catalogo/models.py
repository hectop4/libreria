from django.db import models

# Create your models here.
from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100,default="No Registra")

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    texto = models.TextField()
    puntuacion = models.IntegerField(default=0)

    def __str__(self):
        return f"Reseña de {self.libro.titulo}"
