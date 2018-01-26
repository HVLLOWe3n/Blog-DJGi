from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   # add author in DataBase
    title = models.CharField(max_length=200)                            # add CharField for title
    text = models.TextField()                                           # add TextField for Text in blog
    create_date = models.DateTimeField(default=timezone.datetime.now)   # add date and time to post
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):                                                  # double underscore (__str__)
        return self.title
