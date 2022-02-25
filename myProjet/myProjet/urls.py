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
from django.contrib import admin
from django.urls import path
from Biblio.views import *
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginView.as_view(),name='home'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('inscription/',create_user,name='inscription'),
    path('biblio/download/files/<str:path>/',download,name='download'),
    path('biblio/', login_required(list_epreuve),name = 'index'),
    path('biblio/correction/<int:pk>', login_required(correction_byId),name = 'corrections'),
    path('update/', login_required(update_user),name='update'),
    path('password/', login_required(changePassword_user),name='password'),
]+ static('/biblio/read/files/', document_root='files/')
