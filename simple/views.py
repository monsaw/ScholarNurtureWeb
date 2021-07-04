# Imported modules and libary used for the views

from django.shortcuts import render,redirect
from simple.forms import BaseUserForm,RegistrationForm
from simple.models import Registration,Gallery
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from django.views.generic import (ListView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    return render(request,'simple/index.html',{})

# About us view (function)
def about_us(request):
    return render(request,'simple/about.html',{})

#  Home view for everyone that visit the website (function/class)
class Home(ListView):
    model = Gallery
    template_name = 'simple/home.html'
    context_object_name = 'lists'

#  Registration view for everyone that visit the website (function)
def registration(request):
    registered = False

    if request.method == 'POST':
        baseuser = BaseUserForm(request.POST)
        register = RegistrationForm(request.POST)

        if baseuser.is_valid() and register.is_valid():
            user = baseuser.save(commit = False)
            user.set_password(user.password)
            user.save()


            profile = register.save(commit = False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(baseuser.errors,register.errors)

    else:
        baseuser = BaseUserForm()
        register = RegistrationForm()
    return render(request, 'simple/registration.html', {
    'registered':registered,
    'baseuser':baseuser,
    'register':register
    })

#  Sign view for everyone that visit the website (function)
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('simple:lists')
            else:
                return HttpResponse('Account not Active ! ')
        else:
            return HttpResponse(f'Invalid Login Parameters, Either {username} or {password} is not correct !')
    else:
        return render(request,'simple/login.html',{})


#  Signout view for everyone that visit the website this required sign in first(function)
@login_required
def sign_out(request):
    logout(request)
    return redirect('simple:login')

#  GalleryList view for everyone that visit the website this required sign in first(function)
class GalleryList(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'simple/lists.html'
    model = Gallery
    template_name = 'simple/gallery.html'
    context_object_name = 'lists'

#  GalleryCreate view for everyone that visit the website the required sign in first(function/class), it allows to create new images
class GalleryCreate(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'simple/lists.html'
    model = Gallery
    template_name = 'simple/gallerycreate.html'
    fields = '__all__'

#  GalleryCreate view for everyone that visit the website the required sign in first(function/class), it allows to delete images

class GalleryDelete(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'simple/lists.html'
    model = Gallery
    template_name= 'simple/gallerydelete.html'
    fields = '__all__'

    success_url = reverse_lazy('simple:lists')

#  GalleryCreate view for everyone that visit the website the required sign in first(function/class), it allows to edit existing images
class GalleryUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'simple/lists.html'
    model = Gallery
    template_name = 'simple/gallerycreate.html'
    fields = ('images','description')
