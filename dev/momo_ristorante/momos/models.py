from django.db import models

class Momo(models.Model):
    image_url = models.TextField()
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.title}, price: {self.price}"
