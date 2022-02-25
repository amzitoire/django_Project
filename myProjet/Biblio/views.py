import os
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
    template_name = '#.html' ###Template de add epreuve

    current_user = request.user
    obj = get_object_or_404(
        User,pk=current_user.id,
        # pk=kwargs.get('pk'),
    )

    objet = Epreuve()
    
    form = EpreuveForm(request.POST, request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        objet.intitulet = form.cleaned_data.get('intitulet')
        objet.matiere = form.cleaned_data.get('matiere')
        objet.filiere = form.cleaned_data.get('filiere')
        objet.professeur = form.cleaned_data.get('professeur')
        objet.file = form.cleaned_data.get('file')
        objet.id_user = obj.id
        objet.save()
        return HttpResponseRedirect("/#") ###Template de view epreuve

    context = {
        'form': form,
    }
            
    return render(
            request=request,
            template_name=template_name,
            context=context
        )

def add_correction(request, **kwargs):
    template_name = '#.html' ###Template de add correction
    current_user = request.user
    obj1 = get_object_or_404(
        User,pk=current_user.id,
    )

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
        objet.id_user = obj1.id
        objet.id_epreuve = epreuve.values().get()['id']
        objet.save()
        return HttpResponseRedirect("/#") ###Template de view correction

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
    template_name = 'biblio.html' #######Template de view epreuve
    epreuves = Epreuve.objects.all()
    context ={
        'epreuves' : epreuves,
    }
         
    return render(request=request, template_name=template_name, context=context)

def list_correction(request):
    template_name = 'biblio.html'  ###Template de view correction
    corrections = Correction.objects.all()
    context ={
        'corrections' : corrections,
    }
         
    return render(request=request, template_name=template_name, context=context)
##
def index(request):
    template_name = 'biblio.html'  ###Template de view correction
    corrections = Correction.objects.all()
    epreuves = Epreuve.objects.all()
    context ={
        'corrections' : corrections,
        'epreuves' : epreuves,
    }
    return render(request=request, template_name=template_name, context=context)

def correction_byId(request, **kwargs):
    template_name = 'correction.html'  ###Template de view correction
    obj = get_object_or_404(
        Epreuve,
        pk = kwargs.get('pk')
    )
    corrections = Correction.objects.filter(id_epreuve=obj.id)
    context ={
        'corrections' : corrections,
    }
         
    return render(request=request, template_name=template_name, context=context)
##
def update_epreuve(request, *args, **kwargs):
    template_name = '#.html' ###Template de update epreuve
    obj = get_object_or_404(
        Epreuve,
        pk = kwargs.get('pk')
    )
    if request.method == 'GET':
        form = EpreuveForm(
            initial={
                'intitulet': obj.intitulet,
                'matiere': obj.matiere,
                'filiere': obj.filiere,
                'profeseur': obj.professeur,
                'file': obj.file,
            }
        )
        context = {
            'form': form
        }
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = EpreuveForm(
            request.POST,
            request.FILES,
            initial={
                'intitulet': obj.intitulet,
                'matiere': obj.matiere,
                'filiere': obj.filiere,
                'profeseur': obj.professeur,
                'file': obj.file,
            }
        )
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.intitulet = form.cleaned_data.get('intitulet')
            obj.matiere = form.cleaned_data.get('matiere')
            obj.filiere = form.cleaned_data.get('filiere')
            obj.professeur = form.cleaned_data.get('professeur')
            obj.file = form.cleaned_data.get('file')
            obj.save()
            return HttpResponseRedirect("/#") ###Template de view epreuve
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def update_correction(request, *args, **kwargs):
    template_name = '#.html' ###Template de update correction
    obj = get_object_or_404(
        Correction,
        pk = kwargs.get('pk')
    )
    if request.method == 'GET':
        form = EpreuveForm(
            initial={
                'intitulet': obj.intitulet,
                'file': obj.file,
            }
        )
        context = {
            'form': form
        }
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = EpreuveForm(
            request.POST,
            request.FILES,
            initial={
                'intitulet': obj.intitulet,
                'file': obj.file,
            }
        )
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.intitulet = form.cleaned_data.get('intitulet')
            obj.file = form.cleaned_data.get('file')
            obj.save()
            return HttpResponseRedirect("/#") ###Template de view correction
        return render(
            request=request,
            template_name=template_name,
            context=context
        )

def delete_epreuve(request, *args, **kwargs):
    template_name = '#.html'  ###Template de suppression 
    obj = get_object_or_404(
        Epreuve,
        pk = kwargs.get('pk')
    )
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("#") ###Template de view epreuve
    return render(
        request=request,
        template_name=template_name
        )

def delete_correction(request, *args, **kwargs):
    template_name = '#.html' ######Template de suppression
    obj = get_object_or_404(
        Correction,
        pk = kwargs.get('pk')
    )
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("#") ###Template de view correction
    return render(
        request=request,
        template_name=template_name
        )
    ########################
  
def download(request, *args, **kwargs):
    path=kwargs.get('path')
    file_path = "files/" + path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel"
                                    )
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404