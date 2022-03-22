from django.contrib import admin
from .models import Post, UserPangolin, FriendRequest,LoggedUser, Comentario
# Register your models here.
admin.site.register(Post)
admin.site.register(UserPangolin)
admin.site.register(FriendRequest)
admin.site.register(LoggedUser)
admin.site.register(Comentario)