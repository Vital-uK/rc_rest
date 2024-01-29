from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
    author = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.title


class comment(models.Model):
    text = models.TextField
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('post', related_name='comments', on_delete=models.CASCADE)