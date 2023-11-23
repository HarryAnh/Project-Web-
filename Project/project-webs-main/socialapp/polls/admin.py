from django.contrib import admin
from .models import Post, Profile,FllowersCount,LikePost
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(FllowersCount)
admin.site.register(LikePost)