import array
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Epreuve, User

users: array = []
for user in User.objects.all():
    userelt = (user.id, user.name)
    users.append(userelt)


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

########################################################################################################
class EpreuveForm(forms.ModelForm):

    intitulet = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )

    matiere = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )
    filiere = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )
    professeur = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )
    file = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'type': 'file'
            }

        )
    )
    id_user = forms.ChoiceField(
        required=True,  
        choices=[(x,y) for (x,y) in users],    
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
    
    
    class Meta: 
        model = Epreuve
        fields = [
            'intitulet',
            'filiere',
            'matiere',
            'professeur',
            'file'
        ]
class CorrectionForm(forms.ModelForm):

    intitulet = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )
    file = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'type': 'file'
            }

        )
    )
    id_user = forms.ChoiceField(
        required=True,  
        choices=[(x,y) for (x,y) in users],    
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )
    
    class Meta: 
        model = Epreuve
        fields = [
            'intitulet',
            'file'
        ]