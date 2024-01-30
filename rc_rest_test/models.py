from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(default='', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
#    def __str__(self):
#        return self.title

class comment(models.Model):
    text = models.TextField(blank=False, default='')
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('post', related_name='comments', on_delete=models.CASCADE)

# TODO: models for jwt auth