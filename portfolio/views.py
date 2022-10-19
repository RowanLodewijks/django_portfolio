from django.shortcuts import render

def home(request):
 return render(request, 'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')