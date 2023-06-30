from django.shortcuts import render
from .forms import PizzaSearchForm
from .models import Pizza


def index(request):
    data = {
        'title': 'main page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

