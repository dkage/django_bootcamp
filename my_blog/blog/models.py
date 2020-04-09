from django.db import models
import django.utils.timezone as tz
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=200)
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.DO_NOTHING)
    text = models.TextField()
    create_date = models.DateTimeField(default=tz.now)

    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
