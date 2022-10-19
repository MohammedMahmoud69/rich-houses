from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog_list(request):
    blog_list = Blog.objects.all()

    return render(request , 'blog/blog_list.html' , context={'blogs':blog_list})

def blog_search(request):
    keyword = request.GET.get("search")
    blog_search = Blog.objects.filter(title__icontains=keyword).order_by('-date')
    return render(request, 'blog/blog_search.html', context={'blog_search':blog_search})