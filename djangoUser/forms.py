from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from djangoUser.models import extendedUser
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def startsWith(name):
    for i in name:
        if i in '1234567890':
            raise forms.ValidationError(_("Name cannot have numbers"))

class registrationForm(forms.ModelForm):   
    username=forms.CharField(validators =[startsWith])
    password=forms.CharField(label='Password')
    password2=forms.CharField(label='Confirm Password')
    class Meta:
        model=extendedUser
        fields=['username','first_name','last_name','email','age','address','gender']

    # def clean_username(self):
    #     username=self.cleaned_data['username']
    #     for i in username:
    #         if i in '1234567890':
    #             raise forms.ValidationError(_("Name cannot have numbers"))
    # while using this we dont need to defing validators = function in charfield

class loginForm(AuthenticationForm):
    username=forms.CharField(label='username')
    password=forms.CharField(label='password')