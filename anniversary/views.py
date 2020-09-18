from django.shortcuts import render, redirect

from .models import Anniversary
from .forms import AnniversaryForm

# Create your views here.
def AnniversaryView(request):
    form = AnniversaryForm()
    anniversary = Anniversary.objects.all()

    for event in anniversary:
        event.thumbnail = "https://img.youtube.com/vi/" + event.url[17:] +"/0.jpg"

    if request.method == 'POST':
        if request.POST.get("type") == "add":
            form = AnniversaryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/anniversary')
        elif request.POST.get("type") == "delete":
            anniversary = Anniversary.objects.get(url=request.POST.get("id"))
            anniversary.delete()
            return redirect('/anniversary')

    context = {
        'anniversary': anniversary,
    }

    return render(request, 'anniversary/base.html', context)
