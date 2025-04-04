from django.shortcuts import render
from django.http import HttpResponse

from .models import back_name




def blogging_platfrom(request):
    return render(request, 'html/base.html',{
        'back_name': back_name
    })


# Create your views here.
