from django.db import models

# Create your models here.
class Portfolio(models.Model):
    prt_nombre = models.CharField(max_length=20)
    prt_descripcion = models.CharField(max_length=50)
    prt_plazo_meses = models.IntegerField
    
    def __str__(self):
        return f'{self.prt_nombre} - {self.prt_descripcion}'
    
class Activos(models.Model):
    act_activo = models.CharField(max_length=10)                    #tipo de activo
    act_ticker = models.CharField(max_length=4)                     #ticker
    act_descripcion = models.CharField(max_length=50)                    #descripcion
    act_industria = models.CharField(max_length=20)                 #industria/sector
    act_pais = models.CharField(max_length=20)                      #pais
    act_moneda = models.CharField(max_length=3, default="")         #moneda
    act_mercado = models.CharField(max_length=30, default="")       #mercado donde 
    act_ratio = models.IntegerField                                 #ratio conversion
    
    def __str__(self):
        return f'{self.act_ticker} - {self.act_descripcion}'
    
class Crypto(models.Model):
    cry_ticker = models.CharField(max_length=4)                     #ticker
    cry_descripcion = models.CharField(max_length=50)                    #descripcion
    cry_ratio = models.IntegerField  

    def __str__(self):
        return f'{self.cry_ticker} - {self.cry_descripcion}'

class Bonos(models.Model):
    bon_ticker = models.CharField(max_length=4)                     #ticker
    bon_descripcion = models.CharField(max_length=50)                    #descripcion
    bon_ratio = models.IntegerField  

    def __str__(self):
        return f'{self.bon_ticker} - {self.bon_descripcion}'
        
class Libro(models.Model):
    lib_activo = models.CharField(max_length=10)
    lib_ticker = models.ForeignKey("Activos", on_delete=models.CASCADE) #CharField(max_length=4)
    lib_pcompra = models.FloatField
    lib_cantidad = models.IntegerField
    lib_comision = models.FloatField
    lib_fchcompra = models.DateField