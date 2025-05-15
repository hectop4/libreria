from catalogo.models import Editorial, Libro, Resena

Resena.objects.all().delete()
Libro.objects.all().delete()
Editorial.objects.all().delete()

#Create Editorials
e1=Editorial.objects.create(nombre='Planeta', pais='España')
e2=Editorial.objects.create(nombre='Anagrama', pais='España')
e3=Editorial.objects.create(nombre='Random Penguin House', pais='USA')

#Create Books

l1=Libro.objects.create(titulo='El juego del ángel', autor='Carlos Ruiz Zafón', genero='Ficción', editorial=e1)
l2=Libro.objects.create(titulo='Cien años de soledad', autor='Gabriel García Márquez', genero='Ficción', editorial=e2)
l3=Libro.objects.create(titulo='El amor en los tiempos del cólera', autor='Gabriel García Márquez', genero='Ficción', editorial=e2)
l4=Libro.objects.create(titulo='El psicoanalista', autor='John Katzenbach', genero='Thriller', editorial=e3)
l5=Libro.objects.create(titulo='Angeles y Demonios', autor='Dan Brown', genero='Thriller', editorial=e1)

#Create Reviews
Resena.objects.create(libro=l1, texto='Una historia fascinante que te atrapa desde el principio.',puntuacion=5)
Resena.objects.create(libro=l1, texto='No me gustó, la trama es confusa y aburrida.', puntuacion=2)
Resena.objects.create(libro=l2, texto='Obra maestra de la literatura latinoamericana.', puntuacion=5)
Resena.objects.create(libro=l2, texto='Demasiado largo y difícil de seguir.', puntuacion=1)
Resena.objects.create(libro=l3, texto='Una historia de amor inolvidable y profunda.', puntuacion=5)
Resena.objects.create(libro=l3, texto='No conecté con los personajes, esperaba más.', puntuacion=2)
Resena.objects.create(libro=l4, texto='Un thriller emocionante, no pude dejar de leer.', puntuacion=5)
Resena.objects.create(libro=l4, texto='Predecible y poco original.', puntuacion=2)
Resena.objects.create(libro=l5, texto='Intrigante y lleno de acción, excelente libro.', puntuacion=5)
Resena.objects.create(libro=l5, texto='Demasiado fantasioso y poco creíble.', puntuacion=1)

print("Datos Cargados con Exito")