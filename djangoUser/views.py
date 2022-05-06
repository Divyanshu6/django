from django.shortcuts import render
from djangoUser.forms import registrationForm , loginForm
from django.contrib.auth.views import LoginView

# Create your views here.
def register(request):
    form=registrationForm()
    if request.method=='GET':
        return render(request,'register.html',{'form':form})
    else:
        form_data=registrationForm(data=request.POST)
        print(form_data.errors)
        if form_data.is_valid():
            form_data.save()
            return render(request,'login.html')
        else:
            print("we are here")
            for i in form_data.errors:
                print(i)
            return render(request,'register.html',{'form':form,'form_data':form_data})

# class LoginForm(LoginView):
#     form=loginForm()
