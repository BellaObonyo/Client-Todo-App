from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def submit(request):
    obj = Todo()
    obj.firstname = request.GET['firstname']
    obj.job = request.GET['job']
    obj.secondname = request.GET['secondname']
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def list(request):
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def sortdata(request):
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('-secondname')
    }
    return render(request,'list.html',context=mydictionary)

def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos" : Todo.objects.filter(firstname__contains=q)
    }
    return render(request,'list.html',context=mydictionary)

def edit(request,id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "firstname" : obj.firstname,
        "secondname" : obj.secondname,
        "job" : obj.job,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydictionary)


def update(request,id):
    obj = Todo(id=id)
    obj.firstname= request.GET['firstname']
    obj.secondname= request.GET['secondname']
    obj.job = request.GET['job']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)