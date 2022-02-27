from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def contact(request):
    # Handle the form here
    if request.method == 'POST':
        # for printing
        # print(request.POST['name'])
        # print(request.POST['phone'])
        # print(request.POST['email'])
        # print(request.POST['desc'])

        # for saving into the database
        name  = request.POST['name']
        phone  = request.POST['phone']
        email  = request.POST['email'] 
        desc  = request.POST['desc'] 
        c  = Contact(name=name, phone=phone, email=email, desc=desc)
        c.save()

    return render(request, 'contact.html')