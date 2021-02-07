from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Post
        fields = ("image", "description")


class CommentForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Comment
        fields = ("text",)
