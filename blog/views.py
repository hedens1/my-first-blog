from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # or .filter(published=True), etc.
    return render(request, 'blog/post_list.html', {'posts': posts})   