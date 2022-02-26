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
from turtle import home
from django.contrib import admin
from django.urls import path
from Biblio.views import *
# from . import vie
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('/about', about, name='about'),
    path('/contact', contact, name='contact'),
    path('/privacy-policy', politique, name='politique'),
    path('/terms', using, name='using'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('inscription/',create_user, name='inscription'),
    path('biblio/download/files/<str:path>/',download,name='download'),
    path('biblio/', login_required(list_epreuve),name = 'index'),
    path('biblio/correction/<int:pk>', login_required(correction_byId),name = 'corrections'),
    path('update/', login_required(update_user),name='update'),
    path('password/', login_required(changePassword_user),name='password'),
]