from django.shortcuts import render
from pathlib import Path

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request, *args, **argv):
    return render(request, '500.html') 

def maintenance(request):
    return render(request, 'maintenance.html')