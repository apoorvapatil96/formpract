from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render
from . forms import ContactForm
from . models import ContactData

def contact_view(request):
    if(request.method=="POST"):
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name1=request.POST.get('name','')
            salary1 = request.POST.get('salary', '')
            email1= request.POST.get('email', '')
            location1= request.POST.get('location', '')
            data=ContactData(
                name=name1,
                salary=salary1,
                email=email1,
                location=location1,
            )
            data.save()
            cform=ContactForm()
            return  render(request,'pformapp/contact.html',{'abc': cform})
        else:
            return HttpResponse("invalid form")
    else:
        cform=ContactForm()
        return render(request, 'pformapp/contact.html', {'abc': cform})

