from django.shortcuts import render
from Blog.models import Blog
# Create your views here.
def home_view(request):
    object_list = Blog.objects.all()

    return render(request, 'home.html', {
        'object_list': object_list,
        'nav': 'home'
    })

def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })