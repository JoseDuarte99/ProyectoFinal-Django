from django import forms
from .models import Post, Comments
from django.views.generic.edit import UpdateView


class CommentsForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Ingrese cometario'}),
        label=''
    )

    class Meta:
        model = Comments

        fields = ['text']


class CreatePostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ['title', 'subtitle', 'text', 'category', 'image']


class UpdatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'category', 'image']
