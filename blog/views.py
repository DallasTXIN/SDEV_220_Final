from django.shortcuts import render
from .forms import CarSelectForm
from .models import Car, Part

# Create your views here.
#creat post_list functions, take a request as parameter
def index(request):
    return render(request,'blog/index.html',{})

def about(request):
    return render(request, 'blog/about.html', {})

def parts(request):
    form = CarSelectForm(request.GET or None)#if request empty,empty form
    parts = None#initializes none first
    if form.is_valid(): #https://stackoverflow.com/questions/53594745/what-is-the-use-of-cleaned-data-in-django
        make = form.cleaned_data['make']
        year = form.cleaned_data['year']
        model = form.cleaned_data['model']
        engine = form.cleaned_data['engine']
        if make and year and model and engine:
            car = Car.objects.filter(make=make, year=year, model=model, engine=engine).first()
            if car:
                parts = Part.objects.filter(car=car)
            else:
                parts = []  # No matching car found

    return render(request, 'blog/parts.html', {'form': form, 'parts': parts})