import random

from django.shortcuts import render

from zad.utils import word_generator
from .forms import NumberForm


def index(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            form = NumberForm()
            label = word_generator(number)
            return render(request, 'zad/index.html', {'label': label, 'form': form, 'number': number})
    else:
        form = NumberForm()
    return render(request, 'zad/index.html', {'form': form})


def random_number(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            form = NumberForm()
            label = word_generator(number)
            return render(request, 'zad/index.html', {'label': label, 'form': form, 'number': number})
    else:
        form = NumberForm({'number': random.randrange(-99999999999, 999999999999)})

    return render(request, 'zad/index.html', {'form': form})














