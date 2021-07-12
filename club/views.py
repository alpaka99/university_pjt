from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from club.forms import PostForm,CommentForm
from django.utils import timezone
from club.models import club_post,club_comment
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    latest_post = club_post.objects.order_by('published_date')
    template = loader.get_template('club/base.html')
    context = {
        'latest_post':latest_post
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url='/account/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('club:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'club/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(club_post, pk=pk)
    latest_comment = club_comment.objects.filter(post_pk=pk)
    return render(request, 'club/post_detail.html', {'post': post,'latest_comment':latest_comment})

def post_edit(request, pk):
    post = get_object_or_404(club_post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('club:post_detail', pk=post.pk)
    else:
        if request.user != post.author:
            messages.warning(request, '권한 없음')
            return redirect('club:post_detail', pk=post.pk)
        form = PostForm(instance=post)
    return render(request, 'club/post_edit.html', {'form': form})
def post_delete(request, pk):
    post = get_object_or_404(club_post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect('club:index')
    else:
        if request.user != post.author:
            messages.warning(request, '권한 없음')
            return redirect('club:post_detail', pk=pk)
        form = PostForm(instance=post)
        return render(request, 'club/post_delete.html', {'form': form})

@login_required(login_url='/account/login/')
def comment_new(request,pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.post_pk=pk
            comment.save()
            return redirect('club:post_detail', pk=comment.post_pk)
    else:
        form = CommentForm()
    return render(request, 'club/comment_edit.html', {'form': form})

def comment_edit(request, pk):
    comment = get_object_or_404(club_comment, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            #post.author = request.user
            comment.published_date = timezone.now()
            comment.pk = pk
            comment.save()
            return redirect('club:post_detail', pk=comment.post_pk)
    else:
        if request.user != comment.author:
            messages.warning(request, '권한 없음')
            return redirect('club:post_detail', pk=comment.post_pk)
        form = CommentForm(instance=comment)
    return render(request, 'club/comment_edit.html', {'form': form})

def comment_delete(request, pk):
    comment = get_object_or_404(club_comment, pk=pk)
    if request.method == "POST":
        post_pk = comment.post_pk
        comment.delete()
        return redirect('club:post_detail', pk=post_pk)
    else:
        if request.user != comment.author:
            messages.warning(request, '권한 없음')
            return redirect('club:post_detail', pk=comment.post_pk)
        form = CommentForm(instance=comment)
        return render(request, 'club/comment_delete.html', {'form': form})