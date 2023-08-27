from django.shortcuts import render


# Create your views here.
def Quicknotes(request):
    return render(request, 'quicknotes/quicknotes.html')