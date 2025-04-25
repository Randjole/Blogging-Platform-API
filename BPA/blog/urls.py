from django.urls import path
from . import views

urlpatterns = [
    path('blog',views.blogging_platfrom, name ='blogging-page'),
    path('blog',views.posts, name = 'posts-page'),

]