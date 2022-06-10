from django.db import models

# Create your models here.
class Acreditacion(models.Model):
    contratante = models.CharField(max_length=300)
    codigoAfiliado = models.IntegerField()
    producto = models.CharField(max_length=300)
    numeroDocumento = models.CharField(max_length=100)
    estado = models.BooleanField()
    # idpaciente = 
    # idiafas = 
    # iddocumento =
    class Meta:
        db_table = 'acreditacion';
        managed = True;


