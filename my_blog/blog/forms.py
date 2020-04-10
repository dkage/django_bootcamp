from django import forms
from blog.models import *


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'text_input_class'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea post_content'}),
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        field = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'text_input_class'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
