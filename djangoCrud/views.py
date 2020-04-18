from django.shortcuts import render,redirect
from .models import BookList

# Create your views here.

def index(request):
    books = BookList.objects.all()
    return render(request , 'index.html',{'books':books})


def edit(request):
    pass

def delete(request , id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')