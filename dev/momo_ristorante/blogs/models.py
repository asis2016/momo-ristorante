from django.db import models

class Blog(models.Model):
    title = models.TextField()
    content = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.image_url}"
