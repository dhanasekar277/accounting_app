from django.http import request
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
# Create your views here.

def Logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'account/logout.html')