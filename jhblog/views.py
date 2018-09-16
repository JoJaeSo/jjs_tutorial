# from django.http import HttpResponse
# from django.http import Http404 
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.utils import timezone

from .forms import PostForm
from .models import Post
# Create your views here.

def index(request):
    post_list = Post.objects.order_by('-published_date')
    # print(post_list)
    # template = loader.get_template('jhblog/index.html')
    context = {
        'post_list': post_list
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'jhblog/index.html', context)

def detail(request, pk):
    # try:
        # post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist as e:
        # raise Http404("Post does not exist")
    post = get_object_or_404(Post, pk=pk)

    # return HttpResponse("you're looking at the post %s" % post_id)
    return render(request, 'jhblog/detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('jhblog:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'jhblog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('jhblog:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'jhblog/post_edit.html', {'form': form})

