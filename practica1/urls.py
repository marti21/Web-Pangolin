"""practica1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from pangolin.views import user_Registration, user_profile, home, add_post, get_post, login_user, login_out_user, change_password, change_user_profile, send_friend_request, accept_friend_request, add_friends, see_friends, delete_friend, reject_friend_request,add_friends_search, comment, edit_post, delete_post, first
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration', user_Registration, name="registration"),
    path('profile/<str:username>/', user_profile, name='profile_user'),
    path('home', home, name="home"),
    path('add_post', add_post, name="add_post"),
    path('login', login_user, name="login"),
    path('logOut', login_out_user, name="logout"),
    path('post/<int:post_id>/', get_post, name='post_details'),
    path('change_password', change_password, name='change_password'),
    path('change_profile', change_user_profile, name='change_profile'),
    path('send_friend_request/<str:username>',send_friend_request, name="send friend request"),
    path('accept_friend_request/<int:requestID>',accept_friend_request, name="accept friend request"),
    path('reject_friend_request/<int:requestID>',reject_friend_request, name="reject_friend_request"),
    path('add_friends',add_friends, name="add_friends"),
    path('add_friends_search',add_friends_search, name="add_friends_search"),
    path('see_friends',see_friends, name="see_friends"),
    path('delete_friend/<str:username>',delete_friend, name="delete_friend"),
    path('post2/<int:post_id>/', comment, name='post2'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('', first, name='delete_post'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  