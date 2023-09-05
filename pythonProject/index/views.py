import random

from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def passwordView(request):
    newpassword = ''
    length = int(request.GET.get('length'))
    text = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upper'):
        text.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(length):
        newpassword += text[random.randint(0,len(text)-1)]
    #                                         из html      из python
    return render(request,'password.html', {'newpassword':newpassword})