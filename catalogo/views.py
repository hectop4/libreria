from django.shortcuts import render
from .models import Libro

# Create your views here.
def lista_libros(request):
  libros= Libro.objects.all()
  return render(request,'catalogo/lista.html',{'libros':libros})

def detalle_libro(request):
  libros=Libro.objects.prefetch_related('resena_set').select_related('editorial')
  return render(request,'catalogo/detalle_libro.html',{'libros':libros})