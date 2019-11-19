from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CronForm 
from django.shortcuts import render , redirect
from AssetMgmt.models import Screen
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
import datetime
from django.utils.timezone import utc
from django.utils.timezone import now

class HomeView(LoginRequiredMixin,TemplateView):
    import geocoder
    g = geocoder.ip('me')
    print(g.latlng)
    template_name = 'Echo/maps.html'

@login_required
class LocationView(TemplateView):
    template_name = 'Echo/home.html'

@login_required
def allDeviceView(request):
   form = CronForm()
   screen = Screen.objects.all()
   for curr in screen:
      Screen.objects.filter(activeFlag=curr.activeFlag).update(activeFlag= False)

   if request.method == "POST":
      form = CronForm(request.POST)
      if form.is_valid:
         #redirect to the url where you'll process the input
         return HttpResponseRedirect('register_client') # insert reverse or url
   errors = form.errors or None # form not submitted or it has errors
   return render(request, 'Echo/home.html',{
          'form': form,
          'screen': screen,
   })


class DeviceDetailView(LoginRequiredMixin,DetailView):
  model = Screen

@login_required
def my_view(request):

    # Let's assume that the visitor uses an iPhone...
    request.user_agent.is_mobile # returns True
    request.user_agent.is_tablet # returns False
    request.user_agent.is_touch_capable # returns True
    request.user_agent.is_pc # returns False
    request.user_agent.is_bot # returns False

    # Accessing user agent's browser attributes
    request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    request.user_agent.browser.family  # returns 'Mobile Safari'
    request.user_agent.browser.version  # returns (5, 1)
    request.user_agent.browser.version_string   # returns '5.1'

    # Operating System properties
    request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    request.user_agent.os.family  # returns 'iOS'
    request.user_agent.os.version  # returns (5, 1)
    request.user_agent.os.version_string  # returns '5.1'

    # Device properties
