from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Todo(models.Model):
#     task_name = models.CharField(max_length=200)

class Articles(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='publishedAt')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    urlToImage = models.ImageField(null=True)
    description = models.TextField
    url = models.URLField(null=True)
    favorites = models.ManyToManyField(User, related_name="favorite", default=None, blank=True)
    newmanager = NewManager()

    def __str__(self):
        return self.title

