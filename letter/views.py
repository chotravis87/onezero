import os
from django.shortcuts import render

def LettersView(request):
    context = {
        'events': {
            'lastletter19': {
            'design': 1,
            'name': '1주년',
            'link': os.environ.get('lastletter19'),
            'image': 'https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg'
            }
        }
    }
    return render(request, 'letter/index.html', context=context)