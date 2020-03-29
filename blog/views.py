from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Category, Post
from .forms import PostForm


def blog(request):
    posts = Post.objects.all().order_by('order')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'blog': True,
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'blog': True,
        'post': post,
    }
    return render(request, 'blog/post.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.author = request.user
            post_form.save()
            return redirect('blog')

    else:
        form = PostForm()

    context = {
        'blog': True,
        'title': 'Create Post',
        'form': form,
    }
    return render(request, 'blog/post_form.html', context)


@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')

    else:
        form = PostForm(instance=post)

    context = {
        'blog': True,
        'title': 'Update Post',
        'form': form,
    }
    return render(request, 'blog/post_form.html', context)
