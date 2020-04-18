from django.shortcuts import render
from .models import BookList

# Create your views here.

def index(request):
    books = BookList.objects.all()
    return render(request , 'index.html',{'books':books})
