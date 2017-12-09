from django.contrib import admin
from .models import Artista, Cliente, Compra, Disquera, Genero, Producto

# Register your models here.
admin.site.register(Artista)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Disquera)
admin.site.register(Genero)
admin.site.register(Producto)
