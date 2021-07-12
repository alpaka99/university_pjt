from django import forms
from .models import Review, Review_Comment

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title_text', 'review_text')

class Review_CommentForm(forms.ModelForm):

    class Meta:
        model = Review_Comment
        fields = ('review_comment',)