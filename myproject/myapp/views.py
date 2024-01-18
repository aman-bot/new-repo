from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import User
from .forms import UserForm
from .serializers import UserSerializer
from django.contrib.auth.decorators import login_required

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']

# Create your views here.
@login_required(login_url='/accounts/login/')
def postform(request):
    if request.method=="POST":
        print('inside if')
        print('user who is logged in currently', request.user.username)
        #when request.FILES was not added into the parameter img was not saving into database
        #it was showing only null, so to save img as well we have to pass request.FILES in line no 24
        # also add enctype='multipart/form-data' into <form enctype='multipart/form-data'> posts.html file
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            form.save()
            return HttpResponse("successfully posted")
    else:
        print('inside else empty form')
        form = UserForm
    return render(request, 'posts.html', {'form':form})
        

@login_required(login_url='/accounts/login/')
def home(request):
    data = User.objects.all()
    img = []
    print(data)
    for dd in data:
        img.append(dd.img)
        print('img url',dd.img)
    return render(request, 'feed.html', {'images':img})

@login_required(login_url='/accounts/login/')
def profile_details(request, profile_name):
    users = User.objects.filter(profile_name=profile_name)
    user_list = list(users)
    return render(request, 'profile.html', {'user':user_list})

'''
print(data)
    for dd in data:
        img.append(dd.img)
        print('img url',dd.img)
'''

@login_required(login_url='/accounts/login/')
def house(request):
    data = User.objects.all()
    img = list(data)
    return render(request, 'test.html', {'images':img})


def hack(request):
    return HttpResponse("Your system has been compromised!! your data has been stolen do not visit suspicious website")

