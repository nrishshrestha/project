from django.shortcuts import render

def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    return render(request,'signup.html')

def LoginPage(request):
    return render(request,'login.html')


