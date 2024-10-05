from django import forms

from main.models import Questions
from main.models import Review

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question']

class AnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }