from django.shortcuts import render
from .forms import AdvPostForm
from django.contrib.auth.decorators import login_required
from background_task import background
from django.contrib.auth.models import User

@login_required
def advPost(request):
   form = AdvPostForm()
   if request.method == "POST":
      form = AdvPostForm(request.POST)
      if form.is_valid:
         #redirect to the url where you'll process the input
         return HttpResponseRedirect('adv-register') # insert reverse or url
   errors = form.errors or None # form not submitted or it has errors
   return render(request, 'AdvMgmt/add_new_adv.html',{
          'form': form, })
