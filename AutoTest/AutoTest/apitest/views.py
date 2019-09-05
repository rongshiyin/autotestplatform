from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
# Create your views here.

def test(request):
    return HttpResponse("hello test")

def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active :
            auth.login(request, user)
            request.session['user'] = username
            respose = HttpResponseRedirect('/home/')
            return respose
        else:
            return render(request, 'login.html', {'error' : 'username or password error!!!'})
    
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
