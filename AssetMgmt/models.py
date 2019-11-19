from django.db import models
import datetime
from django.utils.timezone import now
# Asset Information

class Screen(models.Model):
    deviceNumber = models.CharField(max_length=200, verbose_name='Device ID')
#   carRegNumber = models.ForeignKey(Screen, on_delete=models.CASCADE)
    carRegNumber = models.CharField(max_length=6, verbose_name='Registration Number')
    carOwner = models.CharField(max_length=500, verbose_name='Car Owner')
    carDriver = models.CharField(max_length=500, verbose_name='Car Driver')
    carModel = models.CharField(max_length=250, verbose_name='Car Model')
    activeFlag = models.BooleanField(verbose_name='Online')
    longitude = models.DecimalField(max_digits=10 , decimal_places=7 , verbose_name="Longitude",null ='true',default=-26.192900)
    latitude = models.DecimalField(max_digits=10, decimal_places=7 , verbose_name="Latitude",null = 'true' ,default= 28.03050)
    date = models.DateTimeField(default=now, editable=False)
    lastknown = models.CharField(max_length=500, verbose_name='Last Known' , default ="Johannesburg")


    # longitude = models.FloatField(default = 0.000)
    # latitude = models.FloatField(default = 0.000)
   # field for storing the location of the screen

    class meta:
        verbose_name = "Screen Information"

    def __str__(self):
        return self.deviceNumber

    def  get_absolute_url(self):
        return reverse('device-detail', kwargs={'pk':self.pk})

        