# 실제로 작동하는 폼 만들기
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)