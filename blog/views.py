from django.shortcuts import render, redirect
from .models import Blog

# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()

    return render(request, 'blog.html', {
        'blogs': blogs
    })


def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Blog.objects.create(
            title=title,
            description=description
        )

        return redirect('blog_list')

    return render(request, 'blog.html')