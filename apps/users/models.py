from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    PROVINCIAS = [
        ("VI","Arava"), 
        ("AB","Albacete"), 
        ("A","Alacant"), 
        ("AL","Almería"), 
        ("AV", "Ávila"), 
        ("BA","Badajoz"), 
        ("B", "Barcelona"), 
        ("BU", "Burgos"), 
        ("CC", "Cáceres"), 
        ("CA", "Cádiz"), 
        ("CS", "Castelló"), 
        ("CR", "Ciudad Real"), 
        ("CO", "Córdoba"), 
        ("C", "A Coruña"),
        ("CU", "Cuenca"), 
        ("GI", "Girona"), 
        ("GR", "Granada"), 
        ("GU", "Guadalajara"), 
        ("SS", "Gipuzkoa"), 
        ("H","Huelva"), 
        ("HU", "Huesca"), 
        ("IB", "Islas Baleares"), 
        ("J", "Jaén"), 
        ("LR", "La Rioja"), 
        ("GC", "Las Palmas"), 
        ("LE", "León"), 
        ("L",  "Lleida"), 
        ("LU", "Lugo"), 
        ("M", "Madrid"), 
        ("MA","Málaga"), 
        ("MU", "Murcia"), 
        ("NA", "Navarra"), 
        ("OU","Ourense"),
        ("O", "Oviedo"), 
        ("P", "Palencia"),
        ("PO", "Pontevedra"),
        ("SA", "Salamanca"),
        ("TF", "Santa Cruz de Tenerife"),
        ("S", "Santander"),
        ("SG", "Segovia"), 
        ("SE","Sevilla"),
        ("SO", "Soria"), 
        ("T", "Tarragona"),
        ("TE", "Teruel"),
        ("TO", "Toledo"), 
        ("V", "València"), 
        ("VA", "Valladolid"), 
        ("BI", "Bizkaia"),
        ("ZA", "Zamora"), 
        ("Z", "Zaragoza"),
        ("CE", "Ceuta"), 
        ("ML", "Melilla")
    ]   
    username = models.CharField(max_length=150, unique=True, verbose_name="Nombre de empresa")
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    photo = models.ImageField(upload_to='img/user/', default=None, blank=True, verbose_name="Logotipo")
    description = models.TextField(blank=True, verbose_name="Descripción")
    tin = models.CharField(max_length=32, unique=True, blank=True, verbose_name="NIF")
    country = models.CharField(max_length=2, choices=PROVINCIAS, default="L", blank=True, verbose_name="Provincia")
    fiscal_address = models.CharField(max_length=200, blank=True, verbose_name='Dirección fiscal')
    phone = models.CharField(max_length=15, blank=True, verbose_name="Teléfono")
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)


    REQUIRED_FIELDS = ['email','tin', 'fiscal_address', 'phone', 'lat', 'lon', 'photo']

       


