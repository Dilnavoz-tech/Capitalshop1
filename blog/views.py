from django.shortcuts import render
from .models import Post, Tag


def blog_view(request):
    posts = Post.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context=context)


def blog_detail_view(request, pk):
    post = Post.objects.filter(id=pk).first()
    context = {
        'post': post,
        'tags': post.tag.all()
    }
    return render(request, 'blog-details.html', context=context)
