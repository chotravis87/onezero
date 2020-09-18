import os
from django.urls import path
from . import views

if os.environ.get("SIGNUP") == "TRUE": 
    urlpatterns = [
        path('accounts/signup/', views.sign_up, name="signup")
    ]
else:
    urlpatterns = []