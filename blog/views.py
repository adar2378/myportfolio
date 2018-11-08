from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def allblogs(request):
    blogs = Blog.objects.get_queryset().order_by('id')

    paginator = Paginator(blogs, 3)
    print(paginator.page(1).object_list)
    page = request.GET.get('page')
    print(page)
    blogs = paginator.get_page(page)
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
