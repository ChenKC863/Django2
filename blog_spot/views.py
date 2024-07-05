from django.shortcuts import render
from django.http import HttpResponse
from blog_spot.models import Post
# Create your views here.

def index(requests):
    posts = Post.objects.all()
    post_list = list()
    for count, post in enumerate(posts):
        post_list.append("#{}: {}<br><br>".format(str(count),str(post)))
    return HttpResponse(post_list)