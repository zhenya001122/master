from django import forms
from comments.models import Comment, CommentNews


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class CommentNewsForm(forms.ModelForm):
    class Meta:
        model = CommentNews
        fields = ('text',)
