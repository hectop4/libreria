from django.urls import path
from . import views


urlpatterns = [
  path('',views.lista_libros,name="Inicio"),
  path('libros/',views.lista_libros,name="Lista de libros"),
  path('detalle/',views.detalle_libro),

]