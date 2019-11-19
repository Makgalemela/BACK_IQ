from django.contrib import admin
from AssetMgmt.models import Screen

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('id','deviceNumber','carRegNumber','carOwner','carDriver','carModel','activeFlag')
    list_editable = ('deviceNumber','carRegNumber','carOwner','carDriver','carModel','activeFlag')
    list_display_links = ()
    list_filter = ()
    exclude = () 

admin.site.register(Screen, ScreenAdmin)
