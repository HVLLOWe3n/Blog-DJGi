from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import redirect


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


def post_new(request):
    if request.method == "POST":                # Проверка на  <form method='POST/GET'>
        forms = PostForm(request.POST)          # Получаем форму с данными
        if forms.is_valid():                    # Проверка на корректность ввода данных в поля
            post = forms.save(commit=False)     # Не сохраняем модель пока не ввели автора
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        forms = PostForm()

    context = {
        'form': forms
    }

    return render(request, 'blog/post_new.html', context)


def post_edit(request, pk):
    posts = Post.objects.get(pk=pk)

    if request.method == "POST":
        forms = PostForm(request.POST, instance=posts)

        if forms.is_valid():
            post = forms.save(commit=False)  # Не сохраняем модель пока не ввели автора
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        forms = PostForm(instance=posts)

    context = {
        'form': forms
    }
    return render(request, 'blog/post_new.html', context)

