from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'myapp'


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('home/', views.home, name='home'),
    path('test/', views.house, name='house'),
    path('profile/<str:profile_name>/', views.profile_details, name='profile_details'),
    path('hack/', views.hack, name='hack'),
    path('post/create/',views.UserCreateView.as_view(), name='user-list'),
    path('post/', views.UserListView.as_view(), name='post-lists'),
    path('post-form/', views.postform, name='post-form'),
    path('post-the-form/', views.posttheform, name='post-the-form'),
    #path('user/post/', ,name='post'),
]