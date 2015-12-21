from django.db import models

# Create your models here.


class Project(models.Model):
    author =  models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    explanation = models.CharField(max_length=2000)
    image  = models.ImageField()
    project_id =  models.IntegerField()
class Comment(models.Model):
    project_id = models.IntegerField()
    text = models.CharField(max_length=700)
    author = models.ForeignKey('auth.User')
