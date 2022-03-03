"""myProjet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from Biblio.views import *
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    path('',index,name='home'),
   
    #user  
    path('biblio/', login_required(list_epreuve),name ='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('inscription/',create_user,name='inscription'),
    path('update/', login_required(update_user),name='update'),
    path('password/', login_required(changePassword_user),name='password'),
    #dwnload
    path('biblio/download/files/<str:path>/',login_required(download),name='download'),
    #epreuve
    path('biblio/epreuve/ajout', login_required(add_epreuve),name='epreuve_add'),
    path('biblio/epreuve/update/<int:pk>', login_required(update_epreuve),name='epreuve_update'),
    path('biblio/epreuve/delete/<int:pk>', login_required(delete_epreuve),name='epreuve_delete'),
    #correction
    path('biblio/correction/<int:pk>', login_required(correction_byEpreuveId),name ='corrections'),
    path('biblio/correction/ajout/<int:pk>', login_required(add_correction),name='correction_add'),
    path('biblio/correction/update/<int:pk>', login_required(update_correction),name='correction_update'),
    path('biblio/correction/delete/<int:pk>', login_required(delete_correction),name='correction_delete'),
]+ static('/biblio/read/files/', document_root='files/')
