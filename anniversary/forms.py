from django import forms
from .models import Anniversary

class AnniversaryForm(forms.ModelForm):
    class Meta:
        model = Anniversary
        fields = ['datetime', 'url', 'location', 'name']