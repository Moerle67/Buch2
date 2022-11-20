from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status  = Post.Status.PUBLISHED)
    return render(request, 'blog/post/details.html', {'post': post})