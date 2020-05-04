from django.db import models
import datetime


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    creator = models.ForeignKey('user_management.User', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey('user_management.User', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.date.today)

    def save(self, **kwargs):
        self.user = kwargs['user']
        self.post = kwargs['post']
        super(Like, self).save()

    def __str__(self):
        return self.user.email
