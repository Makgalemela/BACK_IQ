from django.db import models
from AssetMgmt.models import Screen

class AssetManagement(Screen):

    class Meta:
    	proxy = True
    	verbose_name = 'Asset Detail'
    	verbose_name_plural = 'Asset Details'
    	
class Updates(models.Model):
    status = models.BooleanField(verbose_name='status')