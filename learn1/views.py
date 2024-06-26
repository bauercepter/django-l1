from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, './about.html')      # relative referencing also works here even though Django knows template dir

