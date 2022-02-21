from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserCreationForm(UserCreationForm,forms.Form):
    is_fromEsmt= forms.BooleanField(required=False,label="Etudiant de L'ESMT",widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
    is_newsletter=forms.BooleanField(required=False,label="S'abonner a la newsletter",widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
    class Meta:
        model = User
        fields = ('email','is_fromEsmt','is_newsletter')


class CustomUserChangeForm(UserChangeForm,forms.Form):
    is_fromEsmt= forms.BooleanField(required=False,label="Etudiant de L'ESMT",widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
    is_newsletter=forms.BooleanField(required=False,label="S'abonner a la newsletter",widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
    class Meta:
        model = User
        fields = ()
class passwordChangeForm(PasswordChangeForm,forms.Form):
    class Meta:
        model=User
        fields = ()
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)