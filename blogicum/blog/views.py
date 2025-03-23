# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Category


def index(request):
    current_time = timezone.now()

    posts = Post.objects.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]

    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    current_time = timezone.now()

    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        pub_date__lte=current_time,
        category__is_published=True
    )

    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    current_time = timezone.now()

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    ).order_by('-pub_date')

    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/category.html', context)
