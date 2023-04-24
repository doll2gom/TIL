from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    posts = Post.objects.all()

    context ={
        'posts':posts,
    }
    return render(request,'posts/index.html',context)

@login_required
def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('posts:index')
    else:
        context = {
            'form': form,
        }
    return render(request,'posts/new.html',context)
@login_required
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post':post,
    }
    return render(request, 'posts/detail.html', context)
@login_required
def update(request,post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail',post.pk)
    else:
        form = PostForm(instance=post)
    
    context ={
        'post':post,
        'form':form,
    }
    return render(request,'posts/update.html',context)
@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return  redirect('posts:index')

@login_required
def category(request, subject):
    # posts_DV= Post.objects.filter(category__contains ='개발')
    # posts_CS = Post.objects.filter(category__contains ='CS')
    # posts_NT = Post.objects.filter(category__contains ='신기술')
    posts = Post.objects.filter(category__contains=subject)
    # # a =[]
    # # for i in posts:
    # #     if i.category == '개발':
    # #         a = i.pk
    # # print(a)
    context = {
        'posts':posts,
        'subject': subject,
        # 'posts_DV': posts_DV,
        # 'posts_CS': posts_CS,
        # 'posts_NT': posts_NT,
    }
    return render(request,'posts/category.html', context)