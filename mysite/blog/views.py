# 用模板输出响应内容
from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Blog, BlogType


def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    # blogs count
    context['blog_count'] = Blog.objects.all().count()
    return render_to_response('blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog/blog_detail.html', context)


def blogs_with_type(request, blog_tpye_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_tpye_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blog/blogs_with_type.html', context)