from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','excerpt','body','tags']
        widgets = {
            'body': TinyMCE()
        }
        