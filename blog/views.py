from django.shortcuts import render
from .forms import CarSelectForm, PartSelectForm
from .models import Car, Part

def index(request):
    return render(request,'blog/index.html',{})

def about(request):
    return render(request, 'blog/about.html', {})

def parts(request):
    car_form = CarSelectForm(request.GET or None)#if request empty,empty form
    part_form = PartSelectForm(request.GET or None)
    car_results = None#initializes none first
    part_results = None
    if 'car_submit' in request.GET and car_form.is_valid(): #https://stackoverflow.com/questions/53594745/what-is-the-use-of-cleaned-data-in-django
        make = car_form.cleaned_data['make']
        year = car_form.cleaned_data['year']
        model = car_form.cleaned_data['model']
        engine = car_form.cleaned_data['engine']
        if make and year and model and engine:
            car = Car.objects.filter(make=make, year=year, model=model, engine=engine).first()
            if car:
                car_results = Part.objects.filter(car=car)
            else:
                car_results = []  # No matching car found
    if 'part_submit' in request.GET and part_form.is_valid():
        name = part_form.cleaned_data['name']
        description = part_form.cleaned_data['description']
        if name and description:
            part = Part.objects.filter(name=name, description=description).first()
            if part:
                part_results = Car.objects.filter(part=part)
            else:
                part_results = []
   
    context = {
        'car_form': car_form,
        'part_form': part_form,
        'car_results': car_results,
        'part_results': part_results,
    }
    return render(request, 'blog/parts.html', context)
