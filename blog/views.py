from django.shortcuts import render

# Create your views here.
#creat post_list functions, take a request as parameter
def index(request):
    return render(request,'blog/index.html',{})
def car(request):
    return render(request, 'blog/car.html', {})
def about(request):
    return render(request, 'blog/about.html', {})