from django.shortcuts import render
from djangoUser.forms import registrationForm

# Create your views here.
def register(request):
    fm=registrationForm()
    return render(request,'register.html',{'fm':fm})
