from django.shortcuts import render
from django.contrib.auth import authenticate, login

def user_login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        
    else:
        #eturn an 'invalid login' error message.
        return  'invalid login' 
