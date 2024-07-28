from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from myApp.models import CustomUser

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profilePic']




    
