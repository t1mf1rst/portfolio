from django.shortcuts import render
from .models import Blog

def allblogs(request):
    allblogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'allblogs':allblogs})
