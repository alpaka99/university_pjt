from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import loader
from .forms import ReviewForm, Review_CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review, Review_Comment
from account.models import Profile

# Create your views here.

def index(request):

    latest_review = Review.objects.order_by('-published_date')
    template = loader.get_template('majorreviews/index.html')
    context = {
        'latest_review' : latest_review
    }
    return HttpResponse(template.render(context, request))

def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    comments = Review_Comment.objects.filter(pk=pk)
    return render(request, 'majorreviews/detail.html', {'review':review, 'comments':comments}) #컨텍스트 적어줄 것

@login_required(login_url='/account/login/')
def edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user != review.author:
        messages.info(request, "권한 없음", extra_tags='safe')
        return redirect('majorreviews:detail', pk=review.pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.published_date = timezone.now()
            review.save()
            return redirect('majorreviews:detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'majorreviews/edit.html', {'form': form})

@login_required(login_url='/account/login/')
def write(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.major_1 = request.user.profile.major1
            review.major_2 = request.user.profile.major2
            review.published_date = timezone.now()
            review.save()
            return redirect('majorreviews:index')
    else:
        form = ReviewForm()
    return render(request, 'majorreviews/write.html', {'form': form})

@login_required(login_url='/account/login/')
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.user != review.author:
        messages.info(request, "권한 없음")
        return redirect('majorreviews:detail', pk=review.pk)

    if request.method == "POST":
        review.delete()
        return redirect('majorreviews:index')
    else:
        form = ReviewForm(instance=review)
        return render(request, 'majorreviews/delete.html', {'form': form})

@login_required(login_url='/account/login/')
def comment_write(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = Review_CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.major_1 = request.user.profile.major1
            comment.major_2 = request.user.profile.major2
            comment.review = review
            comment.published_date = timezone.now()
            comment.save()
            return redirect('majorreviews:detail', pk=review.pk)
    else:
        form = Review_CommentForm()
    return render(request, 'majorreviews/comment_write.html', {'form': form})


@login_required(login_url='/account/login/')
def comment_edit(request, pk):
    comment = get_object_or_404(Review_Comment, pk=pk)
    form = Review_CommentForm(request.POST or None)

    if request.user != comment.author:
        messages.warning(request, "권한 없음")
        return redirect('majorreviews:detail', pk=comment.review.id)

    if request.method == "POST":
        form = Review_CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.published_date = timezone.now()
            comment.save()
            return redirect('majorreviews:detail', pk=comment.review.id)
    else:
        form = Review_CommentForm(instance = comment)
        return render(request, 'majorreviews/comment_edit.html', {'form': form})


'''
def comment_approve(request, pk):
    comment = get_object_or_404(Review_Comment, pk=pk)
    comment.approve()
    return redirect('majorreviews:detail', pk=comment.review.pk)
'''
@login_required(login_url='/account/login/')
def comment_delete(request, pk):
    comment = get_object_or_404(Review_Comment, pk=pk)

    if request.user == comment.author:
        comment.delete()
        return redirect('majorreviews:detail', pk=comment.review.pk)
    else:
        messages.warning(request, "권한 없음")
        return redirect('majorreviews:detail', pk=comment.review.pk)
