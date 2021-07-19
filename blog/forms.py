from django import forms
from django.forms import fields
from .models import Post,Comment,Hashtag #Comment,Hashtag 기능 추가!

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'writer', 'body', 'hashtags', 'image']

# CommentForm 추가
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

# HashtagForm 추가
class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']