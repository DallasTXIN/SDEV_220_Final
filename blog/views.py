from django.shortcuts import render

# Create your views here.
#creat post_list functions, take a request as parameter
def post_list(request):
    return render(request,'blog/about.html',{})