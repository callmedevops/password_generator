from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    Characters = list('abcdefghijklmnoprstuvwxyz')
    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special Characters'):
        Characters.extend(list('~!@#$%^&*()'))
    if request.GET.get('Number'):
        Characters.extend(list('1234567890'))
    length = int(request.GET.get('length', 10))
    generated_password = ''
    for x in range(length):
        generated_password += random.choice(Characters)
    return render(request, 'generator/password.html', {'password': generated_password})
