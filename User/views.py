from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView , FormView
from .models import User
from .forms import UserAdminCreationForm ,  UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# @login_required
class UserCreate(CreateView):
	form_class = UserAdminCreationForm
	template_name = 'users/register.html'
	success_url = 'about/'

@login_required
def about(request):
	return render(request , 'users/temp.html')
# this is custome made registration forms, and user profile creation forms and should works
# welll when it happens it should

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request , 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance =request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,
            instance =request.user.profile)
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated!')
            return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance =request.user)
        p_form = ProfileUpdateForm(instance =request.user.profile)
    context={
    'u_form' : u_form,
    'p_form' : p_form
    }
    return render(request, 'users/Profile.html', context)
