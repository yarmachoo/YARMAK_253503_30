from django import forms

from main.models import Questions

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question']

class AnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
