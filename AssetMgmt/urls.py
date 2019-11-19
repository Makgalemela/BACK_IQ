from django.conf.urls import url
from . background_view import background_view_background
from django.urls import path
urlpatterns = [
	path('background/background/back', background_view_background , name = 'background_task'),

]
