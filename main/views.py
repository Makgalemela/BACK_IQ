from django.shortcuts import render
from django.views.generic import ListView, DetailView
from User.models import User
# Create your views here.


class IndexView(ListView):
	model = User
	template_name = 'main/base.html'
