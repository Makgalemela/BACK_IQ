from django.db.models.signals import post_save
from django.dispatch import receiver
from AssetMgmt.models import Screen
import datetime
from django.utils.timezone import now
import reverse_geocoder as rg
import requests
import json
from django.shortcuts import get_list_or_404, get_object_or_404
from Echo.models import Updates



@receiver(post_save, sender=Screen)
def announce_chnages(sender, instance,update_fields, created, **kwargs):
	
	screen = get_object_or_404(Screen, deviceNumber=instance)
	lat = Screen.objects.get(deviceNumber=instance).latitude
	lng = Screen.objects.get(deviceNumber=instance).longitude
	print(instance)
	res = requests.get('https://ipinfo.io/')
	data = res.json()
	coordinates = (lng,lat)
	results = rg.search(coordinates)
	for i in results:
		pa = i['name'] +", "
		pa +=i['admin1'] +", "
		pa +=i['admin2']
		Screen.objects.filter(deviceNumber=instance).update(lastknown=pa)
		Screen.objects.filter(deviceNumber=instance).update(activeFlag= True)
		Screen.objects.filter(deviceNumber=instance).update(date=datetime.datetime.now())


	
	





	
	