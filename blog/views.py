from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_list_or_404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')   # sort and filter
    context = {
        'post': posts                                                                             # add posts to context
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    context = {
        'post': posts
    }

    return render(request, 'blog/post_detail.html', context)
