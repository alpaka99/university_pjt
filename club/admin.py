from django.contrib import admin

# Register your models here.
from club.models import club_comment,club_post

admin.site.register(club_comment)
admin.site.register(club_post)