from django.shortcuts import render, redirect, HttpResponse
#from django.forms.models import model_to_dict
from django.urls import reverse
from .models import User

# Create your views here.


def home(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)


#def create_user(request):
    #return HttpResponse("this is working too. A new user has been added")

def create_user(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        params = dict()
        
        params['first_name'] = request.POST.get('first')
        params['last_name'] = request.POST.get('last')
        params['email_address'] = request.POST.get('email')
        params['age'] = request.POST.get('age')

        usr =  User.objects.create(**params)
    
    return redirect(reverse('user-home'))