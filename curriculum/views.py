from curriculum.models import major, lecture, class_review
from curriculum.forms import ReviewForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    majors = major.objects.all()
    context = {
        'majors': majors
    }
    return render(request, 'curriculum/index.html', context)


def select_major(request, major_id):
    sel_major = major.objects.get(pk=major_id)
    lecturelist = lecture.objects.filter(lecture_f=major_id)
    year = [1, 2, 3, 4]
    context = {
        'lecturelist': lecturelist,
        'sel_major': sel_major,
        'year': year,
    }
    return render(request, 'curriculum/select_major.html', context)


def review(request, major_id, lecture_id):
    sel_major = major.objects.get(pk=major_id)
    lecturelist = lecture.objects.filter(lecture_f=major_id)
    sel_lecture = lecturelist.get(pk=lecture_id)
    reviewlist = class_review.objects.filter(class_review_f=sel_lecture.id)
    context = {
        'sel_major': sel_major,
        'sel_lecture': sel_lecture,
        'reviewlist': reviewlist,
    }
    return render(request, 'curriculum/class_review.html', context)

@login_required(login_url='/account/login/')
def add_review(request, major_id, lecture_id):
    lecturelist = lecture.objects.filter(lecture_f=major_id)
    sel_lecture = lecturelist.get(pk=lecture_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            class_review = form.save(commit=False)
            class_review.class_review_f = sel_lecture
            class_review.author = request.user
            class_review.major1 = request.user.profile.major1
            class_review.major2 = request.user.profile.major2
            class_review.save()
            return redirect('curriculum:review', major_id=major_id, lecture_id=sel_lecture.id)
    else:
        form = ReviewForm()
    return render(request, 'curriculum/review_write.html', {'form': form})


def del_review(request, major_id, lecture_id, class_review_id):
    lecturelist = lecture.objects.filter(lecture_f=major_id)
    sel_lecture = lecturelist.get(pk=lecture_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        sel_review = class_review.objects.get(pk=class_review_id)
        sel_review.delete()
        return redirect('curriculum:review', major_id=major_id, lecture_id=sel_lecture.id)
    else:
        form = ReviewForm()
    return render(request, 'curriculum/review_delete.html', {'form': form})
