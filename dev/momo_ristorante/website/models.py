from django.db import models

class Booking(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    person = models.IntegerField()
    datestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Setting(models.Model):
    siteurl = models.TextField()
    blogname = models.TextField()
    blogdescription = models.TextField(blank=True)
    users_can_register = models.TextField()
    admin_email = models.TextField()
    mailserver_url = models.TextField()
    mailserver_login = models.TextField()

    def __str__(self):
        return f"{self.siteurl}"

class Homepage(models.Model):
    homepage_id = models.TextField(max_length=10, primary_key=True)
    title = models.TextField(max_length=100)
    subtitle = models.TextField(blank=True)
    content = models.TextField(blank=True)
    link_url = models.TextField(blank=True)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.image_url}"
