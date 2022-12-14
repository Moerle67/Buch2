from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
        status  = Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day)
    return render(request, 'blog/post/details.html', {'post': post})
    
def post_list(request):
    posts = Post.published.all()
    # Pagination with 3 posts per page
    # paginator = 
    return render(request, 'blog/post/list.html', {'posts': posts})