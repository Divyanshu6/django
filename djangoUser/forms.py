from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from djangoUser.models import extendedUser
from django import forms

def startsWith(name):
    for i in name:
        if i in '1234567890':
            raise forms.ValidationError("Name cannot have numbers")

class registrationForm(UserCreationForm):
    city=(
      ('Allahabad','Allahabad'),
      ('Patna','Patna'),
      ('Noida','Noida'),
      ('Ajamgadh','Ajamgadh'),
      ('Bhubneshwar','Bhubneshwar'),
    )
    GENDER_CHOICES = (
   ('Male', 'M'),
   ('Female', 'F'),
)
    username=forms.CharField(validators =[startsWith])
    age=forms.CharField()
    address=forms.ChoiceField(choices=city)
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
    password1=forms.CharField(label='Password')
    password2=forms.CharField(label='Confirm Password')
    class Meta:
        model=extendedUser
        fields=['username','first_name','last_name','email']

class loginForm(AuthenticationForm):
    username=forms.CharField(label='username')
    password=forms.CharField(label='password')