from django import forms
from django.forms import ModelForm, Textarea
from .models import Comments



class ContactForm(forms.Form):
        name=forms.CharField(max_length=50)
        phoneNumber=forms.CharField( max_length=11)
        email=forms.EmailField()
        message=forms.CharField(widget=forms.Textarea)

class CommentForm(ModelForm):
        class Meta:
                model = Comments
                fields = ['text']
                widgets = {'text': Textarea(attrs={'rows': 4}),}


