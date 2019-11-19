from django.contrib import admin
from . models import AssetManagement
from django.shortcuts import render , redirect
from AssetMgmt.models import Screen
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.db.models.signals import post_save
from Serializer.signals import announce_chnages
from django.utils.timezone import utc
from django.utils.timezone import now
import datetime

@admin.register(AssetManagement)
class AssetManagementAdmin(admin.ModelAdmin):
	change_list_template = 'admin/Echo/base.html'
	date_hierarchy = 'date'
	
	class Media:
		js = ('admin/iq_maps.js','admin/unregistered_handlers.js','admin/auto_refresh.js')
		
	def changelist_view(self, request , extra_context = None):

		response = super().changelist_view(
				request,
				extra_context = extra_context,
			)
		try:
			qs = response.context_data['cl'].queryset
		except (AttributeError , KeyError):
			return response

		screen = Screen.objects.all()
		for status in screen:
			post_save.disconnect(announce_chnages, sender=Screen)
			now = datetime.datetime.utcnow().replace(tzinfo=utc)
			timediff = now - status.date
			different_time = timediff.total_seconds()
			if different_time >= 90:
				status.activeFlag = False
				status.save(update_fields=['activeFlag'])
			else:
				status.activeFlag = True;
				status.save(update_fields=['activeFlag'])
		post_save.connect(announce_chnages, sender=Screen)

		response.context_data['summary'] = list(
     		qs
     		.values('id', 'deviceNumber','carRegNumber', 'carOwner' , 
     			'carDriver' ,'carModel' ,'activeFlag', 'longitude', 'latitude','date','lastknown')
     		.order_by('-date')

		)
		list_filter=(
			 'deviceNumber',
			)
		return response

	



