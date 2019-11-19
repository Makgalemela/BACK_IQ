
from django import forms
from .models import Adv
class AdvPostForm(forms.ModelForm):
    class Meta:
        model =  Adv
        fields = ['adTitle', 'clientName', 'adDescription','adMedia', 'timesPlayed' ,'nStoreLocator',]
