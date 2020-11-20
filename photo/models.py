from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse # reverse for model, reverseLazy for view

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos') # primary key of user table
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # add time
    updated = models.DateTimeField(auto_now = True) # update time
    # meta class to add options on model
    class Meta:
        ordering = ['-updated'] #most recent one

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%d-%m-%Y %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])
