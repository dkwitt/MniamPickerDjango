import random

from django.shortcuts import render
from .models import Meals
from django.core.paginator import Paginator
# Create your views here.

def landing(request):
    return render(request, 'picker/landing.html')

def index(request):
    meal_objects = Meals.objects.all()

    #search
    meal_name = request.GET.get('meal_name')
    if meal_name != '' and meal_name is not None:
        meal_objects = meal_objects.filter(name__icontains=meal_name)

    #paginator
    paginator = Paginator(meal_objects, 4)
    page = request.GET.get('page')
    meal_objects = paginator.get_page(page)



    return render(request, 'picker/index.html', {'meal_objects':meal_objects})

def detail(request, id):
    meal_object = Meals.objects.get(id=id)
    return render(request, 'picker/detail.html', {'meal_object':meal_object})

def blind(request):
    meal_object = Meals.objects.get()
    random_meal = random.choice(meal_object)
    return render(request, 'picker/detail.html', {'meal_object':random_meal})