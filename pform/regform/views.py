from django.shortcuts import render


from . forms import  RegistrationForm, LoginForm

from . models import  RegistrationData

from django.http import HttpResponse,HttpResponseRedirect

def registration_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)

        if rform.is_valid():
            first_name=request.POST.get('first_name','')
            last_name = request.POST.get('last_name', '')
            mobile= request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            username= request.POST.get('username', '')
            if(RegistrationData.objects.filter(username=username).exists()):
                return HttpResponseRedirect('/registration',"Invalid Username")
                return HttpResponse("Enter unique username")
            password1 = request.POST.get('password1', '')
            if(RegistrationData.objects.filter(password1=password1).exists()):
                return HttpResponseRedirect('/registration')
                return HttpResponse("Enter unique password")
            password2= request.POST.get('password2', '')
            if(password1!=password2):
                return HttpResponseRedirect('/registration')

            data=RegistrationData(
                first_name=first_name,
                last_name=last_name,
                mobile=mobile,
                email=email,
                username=username,
                password1=password1,
                password2=password2,

            )
            data.save()

            #lform=LoginForm()
            return HttpResponseRedirect('/')
            #return render(request,'regform/login.html',{'lform':lform})

    else:
        rform=RegistrationForm()

        return  render(request,'regform/registration.html',{'rform':rform})
        return  HttpResponseRedirect('/')


def login_view(request):
    if(request.method=="POST"):
        lform=LoginForm(request.POST)
        if(lform.is_valid()):
            uname=request.POST.get('username','')
            pwd=request.POST.get('password1','')
            uname1=RegistrationData.objects.filter(username=uname)

            print(uname1[0])
            pwd1=RegistrationData.objects.filter(password1=pwd)
            print(pwd1[0])
            if(uname1[0]==pwd1[0]):
                return HttpResponse("Valid Details")
            else:
                return HttpResponse("invalid Details")


    else:
        lform=LoginForm()
        return render(request,'regform/login.html',{'lform':lform})
