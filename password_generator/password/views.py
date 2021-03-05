from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    characterrs = list(alphabet)
    lenght = int(request.GET.get('length' , 0))
    thepassword = ''

    if request.GET.get('uppercase'):
        characterrs.extend(list(alphabet.upper()))
    
    if request.GET.get('special'):
        characterrs.extend(list('!"£$%^&*()'))
    
    if request.GET.get('numbers'):
        characterrs.extend(list('0123456789'))

    for x in range(lenght):
        thepassword += random.choice(characterrs)


    return render(request, 'password/home.html', {'password': thepassword})


def about(request):

    return render(request, 'password/about.html')