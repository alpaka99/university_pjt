from django import forms

from curriculum.models import major, lecture, class_review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = class_review
        fields = ('class_review_text',)
