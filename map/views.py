from django.shortcuts import render, redirect
from .models import Cafe
from .forms import CafeForm

def index(request):
    cafe = Cafe.objects.order_by('-id')
    context = {'cafe': cafe}
    return render(request, 'cafe.html', context)

def cafe_create(request):
    if request.method == 'POST':
        form = CafeForm(request.POST)
        if form.is_valid():
            cafe = form.save()
            cafe.save()
            return redirect('/map/')
    else:
        form = CafeForm()
    context = {'form': form}
    return render(request, 'cafe_create.html', context)
