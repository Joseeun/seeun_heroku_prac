from django.contrib import admin
from .models import Post, Comment, Hashtag #Comment, Hahtag 추가

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Hashtag)
