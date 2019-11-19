from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='serialise_api'),
     path('create/', views.DeviceCreateView.as_view(), name=None),
    path('<int:pk>/', views.DeviceDetailView.as_view(), name=None)
]
