from django.db import models
from django.utils import timezone
from django.conf import settings
from account.models import Profile

# Create your models here.
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title_text = models.CharField(max_length=30, null=True)
    major_1 = models.CharField(max_length=20, null = True)
    major_2 = models.CharField(max_length=20, null = True)
    review_text = models.TextField(max_length=200, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.title_text

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Review_Comment(models.Model):
    review_comment = models.TextField(max_length=100, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    major_1 = models.CharField(max_length=20, null= True)
    major_2 = models.CharField(max_length=20, null=True)
    review = models.ForeignKey('majorreviews.Review', on_delete=models.CASCADE, related_name='comments', null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


