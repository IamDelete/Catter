from django.db import models
#TODO: Scris model concurs



class Profesor(models.Model):
    nume = models.CharField(max_length=30)
    prenume = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    parola = models.CharField(max_length=100)
    coordonator_status = models.BooleanField(default=False)
    
class Tester(models.Model):
    nume = models.CharField(max_length=30)
    prenumer = models.CharField(max_length=30)


class Concurs(models.Model):
    nume_concurs = models.CharField(max_length=200)
    judet_concurs = models.CharField(max_length=200)
    
    