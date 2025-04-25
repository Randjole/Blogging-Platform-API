from django.shortcuts import render
from django.http import HttpResponse
from datetime import date




all_posts = [{
    
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "date": date(2025,1,1),
}]




def get_date(post):
    return post['date']

def blogging_platfrom(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'html/index.html',{'posts':latest_posts})

def posts(request):
    return render(request, 'blog/all-posts.html',{'all_posts':all_posts})  


# Create your views here.
