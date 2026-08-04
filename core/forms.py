from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class CriarUsuarioForm(UserCreationForm):
        email = forms.EmailField(required=True, label="E-mail")

        class Meta:
             model = User
             fields = ['username','email']