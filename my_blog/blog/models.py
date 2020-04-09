from django.db import models
from django.utils.timezone import now
import django.utils.timezone as tz


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(default=tz.now)
    published_date = models.DateTimeField(blank=True, null=True)

    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.published_date = tz.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=200)
    post = models.ForeignKey('blog.Post', on_delete=models.DO_NOTHING)
    text = models.TextField()
    create_date = models.DateTimeField(default=tz.now)

    approved_comment = models.BooleanField(default=False)
