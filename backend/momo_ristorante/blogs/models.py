"""
    blogs/model.py
    --------------
    Blog consists of many articles.
    A blog is created by an Employee (employees.models) and it is publicly visible.
"""
from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    """
    Blog model as of v.1.0
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    excerpt = models.TextField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='static/images/blogs/',
                              default='media/default.png',
                              blank=True)
    image_url = models.TextField(blank=True, max_length=20)
    create_date = models.DateField(blank=True)

    def __str__(self):
        return str(self.title)
