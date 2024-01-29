from django.db import models

# Create your models here.
class comment(models.Model):
    text = models.TextField
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(post, related_name='comments')

class comments(models.Model);

class post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blanc=True, default='')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, default='')
    author = models.CharField(max_length=100, blanc=True)
    comments = models.Model()
    def __str__(self):
        return self.title