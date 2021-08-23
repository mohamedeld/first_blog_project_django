from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

import datetime
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    content = RichTextField()
    img = models.ImageField(upload_to="post_img/",default = 'post_img/Capture1.png')
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
