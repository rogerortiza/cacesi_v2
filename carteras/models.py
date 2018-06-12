import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clientes(models.Model):
	class Meta:
		verbose_name="Cliente"
		verbose_name_plural='Clientes'

	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 140)
	razon_social = models.CharField(max_length = 140)
	rfc = models.CharField(max_length=20)
	sucursal = models.CharField(max_length = 140)
	codigo = models.CharField(max_length = 20)
	giro = models.CharField(max_length = 140)
	calle = models.CharField(max_length = 140)
	colonia = models.CharField(max_length=100)
	municipio = models.CharField(max_length = 140)
	estado = models.CharField(max_length = 60)
	cp = models.CharField(blank=True, max_length=5)
	pais = models.CharField(max_length = 60, default="Mexico")
	region = models.IntegerField()
	telefono = models.CharField(max_length = 20)
	email = models.CharField(max_length = 60)
	pagina_web = models.CharField(blank = True, max_length = 140)
	logo = models.ImageField(blank = True, upload_to = "static/images/logosClientes")
	usuario = models.OneToOneField(User, blank = True, null=True, on_delete = models.CASCADE )

	def __str__(self):
		return self.nombre
