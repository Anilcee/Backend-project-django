from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from myApp.models import CustomUser
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import UserCreateForm,CustomUserForm
# Create your views here.


# Create your views here.

def signupaccount(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            user_form = UserCreateForm(request.POST)
            custom_user_form = CustomUserForm(request.POST, request.FILES)
            if user_form.is_valid() and custom_user_form.is_valid():
                first_name = user_form.cleaned_data['first_name']
                last_name = user_form.cleaned_data['last_name']
                username = user_form.cleaned_data['username']
                password1 = user_form.cleaned_data['password1']
                password2 = user_form.cleaned_data['password2']
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password1
                )
                custom_user = CustomUser(user=user, profilePic=custom_user_form.cleaned_data['profilePic'])
                custom_user.save()
                return render(request, 'home.html')
            else:
                return render(request, 'signupaccount.html', {'user_form': user_form,'custom_user_form': custom_user_form,})
        else:
            user_form = UserCreateForm()
            custom_user_form = CustomUserForm()
        return render(request, 'signupaccount.html', {
            'user_form': user_form,
            'custom_user_form': custom_user_form,
        })






def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'loginaccount.html',{'form':AuthenticationForm})
        else:
            user = authenticate(request,
            username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html',{'form': AuthenticationForm(),'error': 'username and password do not match'})
        else:
            login(request,user)
            return redirect('home')
