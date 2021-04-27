from django.shortcuts import render
def home(request):
    return render(request, 'index.html')
def link(request):
    return render(request, 'link.html')