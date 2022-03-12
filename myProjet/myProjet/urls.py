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
from django.urls import path, include
from Biblio.views import *
# from . import vie
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from Biblio.forms import loginForm
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('django.contrib.auth.urls')),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('privacy-policy/', politique, name='politique'),
    path('terms/', using, name='using'),
    path('profil', profil, name='profil'),

#Users  
    # path('accounts/login/', views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True, authentication_form=loginForm), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(template_name='users/logout.html', next_page='home'), name='logout'),
    path('inscription/', create_user, name='inscription'),
    # path('', LogoutView.as_view(), name='logout'),
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', views.LoginView.as_view(template_name='users/login.html', authentication_form=loginForm, redirect_authenticated_user=True), name='login'),
    # path('accounts/password_change/', changePassword_user, name='password_change'),
    path('update_user/', login_required(update_user), name='update'),
    path('change_password/', login_required(changePassword_user), name='password'),


#Epreuve
    path('dashboard/', login_required(list_epreuve, list_correction), name='dashboard'),
    path('new_post/',  login_required(add_epreuve), name='new_post'),
    path('epreuve/<int:pk>', login_required(details_epreuve), name='details_epreuve'),
    path('update/epreuve/<int:pk>', login_required(update_epreuve), name='update_epreuve'),
    path('delete/epreuve/<int:pk>', login_required(delete_epreuve), name='delete_epreuve'),
   
#Correction
    path('add_correction/epreuve/<int:pk>',  login_required(add_correction), name='add_correction'),
    path('correction/<int:pk>', login_required(correction_byId),name = 'corrections'),
    path('view_correction/', (correction_byId), name ='view_correction'),
    path('update/correction/<int:pk>/', login_required(update_correction), name='update_correction'),
    path('list_correction/<int:pk>', login_required(list_correction), name='list_correction' ),
    path('delete/correction/<int:pk>', login_required(delete_epreuve), name='delete_correction'),

    path('biblio/download/files/<str:path>/',login_required(download), name='download'),
    
    # path('biblio/download/files/<str:path>/', login(download), name='download'),
    path('biblio/', login_required(list_epreuve), name = 'index'),
] + static('/biblio/read/files/', document_root='files/')