from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User 
from django.db import models
from .models import Screen


class  DeviceRegistrationForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = Screen
        fields = ['deviceNumber', 'carRegNumber', 'carOwner', 'carDriver','carModel', 'activeFlag']

    # def __init__(self, *args , **kwargs):
    #     # super(UserCreationForm, self).__init__(*args, **kwargs)
    #     for fieldname in ['username' ,'email','password1']:
    #         self.fields[fieldname].help_text = None
     

# class DeviceUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
        # fields = ['image']