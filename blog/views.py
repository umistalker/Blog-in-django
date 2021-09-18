from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('date')
    return render(request, 'all_blogs.html', {'blogs': blogs})
