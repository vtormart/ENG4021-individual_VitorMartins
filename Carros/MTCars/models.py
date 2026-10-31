from django.db import models

# Create your models here.

class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME') # Field name made 
    mpg = models.FloatField(db_column='MPG') # Field name made 
    cyl = models.IntegerField(db_column='CYL') # Field name 
    disp = models.FloatField(db_column='DISP') # Field name 
    hp = models.IntegerField(db_column='HP') # Field name made 
    wt = models.FloatField(db_column='WT') # Field name made 
    qsec = models.FloatField(db_column='QSEC') # Field name 
    vs = models.IntegerField(db_column='VS') # Field name made 
    am = models.IntegerField(db_column='AM') # Field name made 
    gear = models.IntegerField(db_column='GEAR') # Field name 
    
    class Meta:
        managed = True
        db_table = 'MTCars'             # nome da tabela
        ordering = ['id']               # ordenação default
        verbose_name_plural = "MTCars"  # plural de MTCars

    def __str__(self):
        '''
        Retorna a representação em string do objeto MTCars.
        Por exemplo, o que vai ser listado na 
        interface de admin.
        '''
        return "Modelo: " + self.name

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'MTCars',   # linha acrescentada
]