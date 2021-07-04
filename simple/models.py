from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Registration(models.Model):
    choice = (('M','Male'),('F','Female'))
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length = 40, choices = choice , default = 'Male')
    DateOfBirth = models.DateTimeField(blank = True, null = True)
    def __str__(self):
        return self.user.username




class Gallery(models.Model):
    owner = models.CharField(max_length = 50, )
    images = models.ImageField(upload_to = 'picture/' , blank = False)
    description = RichTextField()

    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse('simple:lists')
