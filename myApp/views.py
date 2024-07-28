from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render,redirect
from .models import OurServices,PetGallery,Pets,Comments,Team,HomeSlide
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm,CommentForm
from django.contrib.auth.decorators import login_required   
from django.core.mail import send_mail
import smtplib


       

def home(request):
    services=OurServices.objects.all()
    slides=HomeSlide.objects.all()
    context={'services':services,'slides':slides}
    return render(request,'home.html',context)

def service(request):
    services=OurServices.objects.all()
    return render(request,'service.html',{'services':services})

def petGallery(request):
    images=PetGallery.objects.all()
    return render(request,'pet.html',{'images':images})

def clinic(request):
    team = Team.objects.all()
    comments = Comments.objects.all()
    context = {'team': team, 'comments': comments}
    return render(request, 'clinic.html', context)


def contact(request):
    form = ContactForm()

    if request.method=='POST':
        form=ContactForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            phoneNumber=form.cleaned_data['phoneNumber']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']

            try:
                send_mail(
        'Contact Form: ', 
        f'Name: {name}\nPhone Number: {phoneNumber} \n Message:{message}\n Mail:{email}',
        'anilcengizz75@gmail.com',
        ['c88f65ba4b-5ef680@inbox.mailtrap.io'],
        fail_silently=False,
    )
            except smtplib.SMTPException as e:
                print("Error :", e)
            
        return render(request, 'contact.html', {'form': form})
    else:
        # Render the contact form
        return render(request, 'contact.html', {'form': form})



def buy(request):
    pets = Pets.objects.all()  # veritabanındaki tüm verileri alın
    paginator = Paginator(pets, 5)  # verileri 5'er 5'er gruplara bölün

    # URL'den gelen 'page' değişkenine göre verileri sayfalara bölün
    page = request.GET.get('page')
    try:
        pets = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pets = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pets = paginator.page(paginator.num_pages)

    context = {
        'pets': pets,
    }
    return render(request, 'buy.html', context)


@login_required
def createComment(request):
    if request.method == 'GET':
        return render(request, 'createComment.html',{'form':CommentForm()})
    else:
        
        form=CommentForm(request.POST)
        newComment=form.save(commit=False)
        newComment.user=request.user
        newComment.save()
        return render(request,'home.html')

