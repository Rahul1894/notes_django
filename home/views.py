from django.shortcuts import render # type: ignore
from django.http import HttpResponse# type: ignore
from datetime import datetime# type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.views.generic import TemplateView # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.contrib.auth.views import LoginView,LogoutView #type:ignore
from django.views.generic.edit import CreateView #type:ignore
from django.contrib.auth.forms import UserCreationForm #type:ignore
from django.shortcuts import redirect #type:ignore
# Create your views here.

# def home(request):  #every time it will receice an request, it will return hello world 
#     return HttpResponse('Hello world!')

#but how do we know that home function will receice requests that's why we will import this file in urls.py in smartnotes  

# def home(request):
#     return render(request,'home/welcome.html',{})  # empty brackets are used to pass down informtion to that html file 

# def home(request):
#     return render(request,'home/welcome.html',{'today':datetime.today()})  # we can pass information like dictionary in key value pairs and that key is used in html file 


# @login_required                  # this would make the endpoint authorized needed to login   and will show 404 error
# def authorized(request):
#     return render(request,'home/authorized.html',{})

class Signupview(CreateView):
    form_class=UserCreationForm
    template_name='home/register.html'
    # success_url='/smart/notes'
    success_url='/login'

    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(self,request,*args,**kwargs)

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'

class LoginInterfaceView(LoginView):
    template_name='home/login.html'

class HomeView(TemplateView):
    template_name='home/welcome.html'
    extra_context={'today':datetime.today()}

class authorizedView(LoginRequiredMixin,TemplateView):
    template_name='home/authorized.html'
    login_url='/admin'


# @login_required(login_url='/admin')     # but we don't want them to see 404 error and instead redirect them to admin login url then we do this
# def authorized(request):
#     return render(request,'home/authorized.html',{})
