from django.shortcuts import render
from blog.models import Category, Post_home, banner, Video
from django.db.models import Q


def home(request):
    all_post = Post_home.objects.filter(status='Published').order_by('created_at')
    all_categories = Category.objects.all()
    all_banners =  banner.objects.filter(status='Published')
    all_video = Video.objects.filter(status='Published')

    context = {

        'cat': all_categories,
        'post': all_post,
        'banner' : all_banners,
        'video': all_video,
    }
    return render(request, 'blog.html', context)

def show_post_detalhe(request, slug):
    all_post = Post_home.objects.filter(~Q(urlAmigavel = slug),status='Published').order_by('created_at')
    all_categories = Category.objects.all()
    by_post = Post_home.objects.filter(urlAmigavel=slug)

    context = {

        'cat': all_categories,
        'by_post': by_post,
        'post': all_post,


    }

    return render(request, 'blog-noticia.html', context)