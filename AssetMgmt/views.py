from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView , FormView
from .models import Screen
from django.contrib.auth.decorators import login_required
from .forms import DeviceRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin

@login_required
def registerAsset(request):
    if request.method == 'POST':
        form = DeviceRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            deviceNumber = form.cleaned_data.get('deviceNumber')
            messages.success(request, f'Account created for {deviceNumber }!')
            return redirect('user_login')
    else:
        form = DeviceRegistrationForm()
    return render(request , 'AssetMgmt/asssets_view.html', {'form': form})