from django import forms

from club.models import club_post,club_comment

class PostForm(forms.ModelForm):

    class Meta:
        model = club_post
        fields = ('title', 'text', 'image',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = club_comment
        fields = ('text',)