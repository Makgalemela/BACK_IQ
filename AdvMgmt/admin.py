from django.contrib import admin
from .models import Adv

class AdvAdmin(admin.ModelAdmin):
    list_display = ('id','adTitle','adDescription','timesPlayed','clientName')
    list_display_links = ('id','adDescription')
    list_filter = ()
    list_editable = ('adTitle' ,'clientName')
    readonly_fields = ['id','timesPlayed']
    exclude = ['id']

admin.site.register(Adv, AdvAdmin)
