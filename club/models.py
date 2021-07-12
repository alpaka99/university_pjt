from django.db import models
from django.conf import settings
from django.utils import timezone

class club_comment(models.Model):
    text = models.CharField(max_length=400,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.text
    post_pk = models.IntegerField(null=True)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class club_post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='image', null = True , blank = True)
    def __str__(self):
        return self.title
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()