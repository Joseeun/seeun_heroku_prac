from django.http import request
from .forms import PostForm, HashtagForm, CommentForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Hashtag, Post
from django.utils import timezone

# Create your views here.

#메인 페이지
def main(request):
    return render(request,'blog/main.html')


#글쓰기 함수
def create(request):

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = PostForm
        return render(request, 'blog/write.html', {'form':form})

def blogform(request, blog=None):
    if request.method == 'POST':
        form = PostForm(request.POST, instance=blog)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.datetime.now()
            post.save()
            form.save_m2m()
            return redirect('read')
    else:
        form = PostForm(instance=blog)
        return render(request, 'blog/write.html', {'form':form})

def edit(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method =='POST':
        form = PostForm(request.POST, isinstance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')

    else:
        form = PostForm(instance=post)
        return render(request,'blog/edit.html',{'form':form})

#삭제하기 함수
def delete(request,id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('read')


#디테일 페이지
def detail(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail',id)
    else:
        form=CommentForm()
        return render(request, 'blog/detail.html',{'post':post, 'form':form})


def read(request):
    posts = Post.objects
    hashtags = Hashtag.objects
    return render(request, 'blog/read.html',{'posts':posts, 'hashtags':hashtags})

#해쉬 태그 함수
def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시 태그 입니다. "
                return render(request, 'blog/hashtag.html', {'form':form, "error_message":error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('read')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'blog/hashtag.html', {'form':form})

def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'search.html', {'hashtag':hashtag})
