from django.contrib.auth.models import User
from django.db import models

class OAuth2Token(models.Model):
    name = models.CharField(max_length=40)
    token_type = models.CharField(max_length=20)
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    # oauth 2 expires time
    expires_at = models.IntegerField()
    # ...
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def to_token(self):
        return dict(
            access_token=self.access_token,
            token_type=self.token_type,
            refresh_token=self.refresh_token,
            expires_at=self.expires_at,
        )

class Post(models.Model):
    title = models.CharField('title', max_length=200)
    subject = models.CharField('subject_code', max_length=200)
    modification_date = models.DateTimeField('modification_date')
    text = models.TextField('text')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
