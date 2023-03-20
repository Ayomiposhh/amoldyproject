from django import forms
from amoldy_app.models import *




class ContactForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    email = forms.EmailField(label='Email :', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    message =forms.CharField(label='Message :', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    
    class Meta():
     model=Contact
     fields= ['name', 'email', 'message']
    