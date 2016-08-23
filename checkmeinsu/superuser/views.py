from django.shortcuts import render


def superuser(request):
    return render(request, 'superuser.html')

def userpage(request):
    return render(request, 'userpage.html')

def configuration(request):
    return render(request, 'configurationpage.html')

def userform(request):
    return render(request, 'userform.html')

# Create your views here.
