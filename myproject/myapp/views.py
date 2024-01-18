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

# Create your views here. this postform will not save username
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

'''
when you create form of a model and do form.save() then only those field you mentioned in form like in User model's form
we have only img and title files so only these 2 fields value will be stored and profile_name will be null
so to save profile_name as username[who logged in] we fetching details from form() and request to get username
and then created a User obj and then saving it p.save() this will save profile_name, img, title to the database 
'''

@login_required(login_url='/accounts/login/')
def posttheform(request):
    if request.method=="POST":
        print('inside if')
        print('user who is logged in currently', request.user.username)
        #when request.FILES was not added into the parameter img was not saving into database
        #it was showing only null, so to save img as well we have to pass request.FILES in line no 24
        # also add enctype='multipart/form-data' into <form enctype='multipart/form-data'> posts.html file
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            u_name = request.user.username
            imgs = form.cleaned_data['img']
            titles = form.cleaned_data['title']
            p = User(profile_name=u_name, img=imgs, title=titles)
            # here instead of form.save() i created a User model object because in form we don't user naeme to be
            #input by user, instead we want it to pickup automatically because user is logged in
            p.save()
            return redirect("/home/")
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

