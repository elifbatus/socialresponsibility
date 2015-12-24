from django.db import models

# Create your models here.


class Project(models.Model):
    creator = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    aciklama = models.TextField()
    pid = models.IntegerField()
class Comments(models.Model):
    pid = models.IntegerField()
    author = models.ForeignKey('auth.User')
    text = models.TextField()
<<<<<<< Updated upstream
=======


>>>>>>> Stashed changes
