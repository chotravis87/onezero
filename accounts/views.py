from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    context['form'] = form
    return render(request, 'registration/register.html', context)