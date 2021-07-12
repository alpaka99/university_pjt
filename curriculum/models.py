from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class major(models.Model):
    major_name = models.CharField(max_length=10)

    def __str__(self):
        return self.major_name


class lecture(models.Model):
    lecture_f = models.ForeignKey(major, on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=20)
    professor = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    book = models.CharField(max_length=50)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.lecture_name


class class_review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    major1 = models.CharField(max_length=20, null= True)
    major2 = models.CharField(max_length=20, null=True)
    class_review_f = models.ForeignKey(lecture, on_delete=models.CASCADE)
    class_review_text = models.TextField(max_length=1000, default=' ')
    approved_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.class_review_text

    def approve(self):
        self.approved_comment = True
        self.save()