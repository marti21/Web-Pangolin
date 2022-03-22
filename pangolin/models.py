from email.policy import default
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime, date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.signals import user_logged_in, user_logged_out

class UserPangolin(User):
    my_date_field = models.DateField(default=date.today())
    image = models.ImageField(upload_to='userImages',blank=True, default="basic_user.jpg")
    friends = models.ManyToManyField("UserPangolin", blank=True)

    def get_absolute_url(self):
        return reverse('profile_user', kwargs={'username':self.username})

    def get_email(self):
        return self.email


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField('created',auto_now_add=True) 
    image = models.ImageField(upload_to='userImages',blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'post_id':self.id})

    def get_absolute_url2(self):
        return reverse('profile_user', kwargs={'username':self.author})

    def get_absolute_url3(self):
        return reverse('post2', kwargs={'post_id':self.id})

    def get_absolute_url4(self):
        return reverse('edit_post', kwargs={'post_id':self.id})

    def get_absolute_url5(self):
        return reverse('delete_post', kwargs={'post_id':self.id})
    
    def devolverPost(self):
        return self


class Comentario(models.Model): 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField('created',auto_now_add=True)

    def __str__(self):
        return self.text


class FriendRequest(models.Model):
    from_user = models.ForeignKey(UserPangolin,related_name='from_user', on_delete=models.CASCADE, null=True)
    to_user = models.ForeignKey(UserPangolin, related_name='to_user',on_delete=models.CASCADE, null=True)


class LoggedUser(models.Model):
    user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username

    def login_user(sender, request, user, **kwargs):
        LoggedUser(user=user).save()

    def logout_user(sender, request, user, **kwargs):
        try:
            u = LoggedUser.objects.get(user=user)
            u.delete()
        except LoggedUser.DoesNotExist:
            pass

    user_logged_in.connect(login_user)
    user_logged_out.connect(logout_user)