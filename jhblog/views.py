# from django.http import HttpResponse
# from django.http import Http404 
from django.shortcuts import get_object_or_404, render
from django.template import loader

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

def detail(request, post_id):
    # try:
        # post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist as e:
        # raise Http404("Post does not exist")
    post = get_object_or_404(Post, pk=post_id)

    # return HttpResponse("you're looking at the post %s" % post_id)
    return render(request, 'jhblog/detail.html', {'post':post})