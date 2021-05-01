"""
    Blog form
"""
from django.forms import ModelForm, DateInput, EmailInput

from .models import Blog


class BlogForm(ModelForm):
    """
        Blog form class as of v.1.0
    """

    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'excerpt', 'content','image', 'create_date']
        widgets = {
            'title': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Blog title'
            }),
            'create_date': DateInput(attrs={'type': 'date'})
        }
        labels = {
            'title': 'Blog title'
        }
        help_texts = {
            'title': 'Please give the blog title.'
        }
