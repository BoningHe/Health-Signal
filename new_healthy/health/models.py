from django.db import models

# Create your models here.
class emg(models.Model):
    data = models.IntegerField(null=False)

class spo2(models.Model):
    data = models.IntegerField(null=False)

class heart_rate(models.Model):
    data = models.IntegerField(null=False)
