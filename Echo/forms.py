
from AssetMgmt.models import Screen
from django import forms

class CronForm(forms.Form):
    DeviceId = forms.ModelChoiceField(queryset=Screen.objects.all().order_by('deviceNumber'), required=True)

