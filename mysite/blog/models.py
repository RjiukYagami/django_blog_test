from django.db import models
from django.utils import timezone


# Create your views here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.DateField(default=timezone.now)
    publish_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.publis_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
