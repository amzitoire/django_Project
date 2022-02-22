from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

from .models import *
from .forms import *

# Create your views here.
class LoginView(TemplateView):

  template_name = 'index.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'index.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)
  
def create_user(request,*args,**kwargs):
    template_name= 'inscription.html'
    if request.method == 'GET':
        form = CustomUserCreationForm(
            initial={
                
            }
        )
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =CustomUserCreationForm(
           request.POST,
           request.FILES,
           initial={
              
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
          print(form.cleaned_data)
          form.save()
          return redirect('home')
        return render(request=request,template_name=template_name,context=context,)
      
def update_user(request,*args,**kwargs):
    template_name= 'update_user.html'
    current_user = request.user
    
    
    obj = get_object_or_404(
        User,pk=current_user.id,
        # pk=kwargs.get('pk'),
    )
    if request.method == 'GET':
        form = CustomUserChangeForm(
            initial={
              'email': obj.email,
              'is_active': obj.is_active,
              'is_fromEsmt': obj.is_fromEsmt,
              'is_newsletter': obj.is_newsletter,
          
            }
        )
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =CustomUserChangeForm(
           request.POST,
           request.FILES,
           initial={
              'email': obj.email,
              'is_active': obj.is_active,
              'is_fromEsmt': obj.is_fromEsmt,
              'is_newsletter': obj.is_newsletter,
             
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
          print(form.cleaned_data)
          obj.is_fromEsmt = form.cleaned_data['is_fromEsmt']
          obj.is_newsletter = form.cleaned_data['is_newsletter']
          obj.save()
          return redirect('home')
        return render(request=request,template_name=template_name,context=context,)
      
def changePassword_user(request,*args,**kwargs):
    template_name= 'update_password.html'
    current_user = request.user
    
    
    obj = get_object_or_404(
        User,pk=current_user.id,
    )
    if request.method == 'GET':
        form = passwordChangeForm(obj)
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =passwordChangeForm(obj,
           request.POST,
           request.FILES,
             initial={
            
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
          print(form.cleaned_data)
          user = form.save
          update_session_auth_hash(request, user)  # Important!
          return redirect('home')
        return render(request=request,template_name=template_name,context=context,)

##################################################################################
def add_epreuve(request, **kwargs):
    template_name = 'add-epreuve.html'

    objet = Epreuve()
    
    form = EpreuveForm(request.POST, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        objet.intitulet = form.cleaned_data.get('intitulet')
        objet.matiere = form.cleaned_data.get('matiere')
        objet.filiere = form.cleaned_data.get('filiere')
        objet.professeur = form.cleaned_data.get('professeur')
        objet.file = form.cleaned_data.get('file')
        objet.id_user = form.cleaned_data.get('id_user')
        objet.save()
        return HttpResponseRedirect("/epreuve")

    context = {
        'form': form,
    }
            
    return render(
            request=request,
            template_name=template_name,
            context=context
        )

def add_correction(request, **kwargs):
    template_name = 'add-correction.html'

    obj = get_object_or_404(
        Epreuve,
        pk = kwargs.get('pk')
    )
    objet = Correction()
    epreuve = Epreuve.objects.filter(id=obj.id)
    
    form = CorrectionForm(request.POST, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        objet.intitulet = form.cleaned_data.get('intitulet')
        objet.file = form.cleaned_data.get('file')
        objet.id_user = form.cleaned_data.get('id_user')
        objet.id_epreuve = epreuve.values().get()['id']
        objet.save()
        return HttpResponseRedirect("/list_profil")

    context = {
        'epreuve': epreuve,
        'form': form,
    }
            
    return render(
            request=request,
            template_name=template_name,
            context=context
        )

def list_epreuve(request):
    template_name = 'views.html'
    epreuves = Epreuve.objects.all()
    context ={
        'epreuves' : epreuves,
    }
         
    return render(request=request, template_name=template_name, context=context)

def list_correction(request):
    template_name = 'views.html'
    corrections = Correction.objects.all()
    context ={
        'corrections' : corrections,
    }
         
    return render(request=request, template_name=template_name, context=context)

