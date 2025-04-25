from django.shortcuts import render
from django.http import HttpResponse

from .models import back_name


all_posts = {
    
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"]
}




def blogging_platfrom(request):
    return render(request, 'html/index.html',{

    })
def posts(request):
    return render(request, 'blog/all-posts.html',{'all_posts':all_posts})  


# Create your views here.
