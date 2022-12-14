from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):

    # class NewManager(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter(status='publishedAt')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    urlToImage = models.URLField(null=True)
    description = models.TextField
    url = models.URLField(null=True)
    #favorites = models.ManyToManyField(User, related_name="favorite", default=None, blank=True)
    # newmanager = NewManager()

    def __str__(self):
        return self.title


class Profile(models.Model):
    profileId = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)

    def __str__(self):
        return f'{self.profileId}'


