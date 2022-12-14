from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class sensortemperatura (models.Model):
    nombre= models.CharField(max_length=45, null=False)
    tempmax= models.IntegerField(null=False)
    tempmin= models.IntegerField(null=False)
    tempactual= models.IntegerField(null=False)

    def _str_(self):
        return "%s" % (self.nombre)

    class Meta:
        app_label= 'app'


class sensorhumedad (models.Model):
    nombre= models.CharField(max_length=45, null=False)
    tiempoderiego= models.IntegerField(null=False)
    humedadactual= models.IntegerField(null=True)
            
    def _str_(self):
        return "%s" % (self.nombre)

    class Meta:
        app_label= 'app'


class camaras (models.Model):
    nombre= models.CharField(max_length=45, null=False)

    def _str_(self):
        return "%s" % (self.nombre)

    class Meta:
        app_label= 'app'

class administrador (models.Model):
    numerocultivos= models.IntegerField(null=False)

    user = models.OneToOneField(
        User,
        related_name='administrador',
        null=True,
        primary_key=False,
        on_delete=models.PROTECT
    )
    

    def _str_(self):
        return "%s %s" % (self.user)

    class Meta:
        app_label= 'app'


class cultivo (models.Model):
    nombre= models.CharField(max_length=45, null=False)
    fecha=models.DateField(auto_now=False, auto_now_add=False, null=False)
    localidad=models.CharField(max_length=45, null=False)


    administrador= models.ForeignKey(
        administrador,
        related_name='administrador',
        null=False,
        on_delete=models.PROTECT
    )

    sensortemperatura= models.ForeignKey(sensortemperatura,
        related_name='sensor_temperatura',
        null=False,
        on_delete=models.PROTECT
    )
    sensorhumedad= models.ForeignKey(sensorhumedad,
        related_name='sensor_humedad',
        null=False,
        on_delete=models.PROTECT
    )
    camarasid= models.ForeignKey(camaras,
        related_name='camaras',
        null=False,
        on_delete=models.PROTECT
    )

    def _str_(self):
        return self.nombre

    class Meta:
        app_label= 'app'

