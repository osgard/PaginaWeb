from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
	
class Cliente(models.Model):
	usuario = models.ForeignKey(User)
		
	def __str__(self):
		return self.usuario.username
            
class Genero(models.Model):
	nombreG = models.CharField(max_length=20)
	
	def __str__(self):
            return self.nombreG
	
class Artista(models.Model):
	nombreA = models.CharField(max_length=30)
	
	def __str__(self):
            return self.nombreA
            
class Disquera(models.Model):
	nombreD = models.CharField(max_length=30)
	
	def __str__(self):
            return self.nombreD
            
class Producto(models.Model):
	genero = models.ForeignKey(Genero)
	artista = models.ForeignKey(Artista)
	disquera = models.ForeignKey(Disquera)
	nombreP = models.CharField(max_length=30)
	precio = models.FloatField()
	portada = models.ImageField(upload_to='galeria',null=True, blank=True)
	stock = models.IntegerField(blank=True,null=True)
	infor = models.TextField(null=True)
	published_date = models.DateTimeField(
                blank=True, null=True)
                
	def publish(self):
			self.published_date = timezone.now()
			self.save()
	
	def __str__(self):
			return self.nombreP
			
class Compra(models.Model):
	productoC = models.ForeignKey(Producto)
	clienteC = models.ForeignKey(User)
	total = models.FloatField(blank=True,null=True)
	cantidad = models.FloatField(blank=True,null=True)
	fecha_compra = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
			self.fecha_compra = timezone.now()
			self.save()
	
	def __str__(self):
			return self.clienteC.username
	
            

