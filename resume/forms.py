from django import forms

class contactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=20)
    msg= forms.CharField(max_length=100)
