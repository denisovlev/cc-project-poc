from django.db import models

class OAuth2Token(models.Model):
    name = models.CharField(max_length=40)
    token_type = models.CharField(max_length=20)
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    # oauth 2 expires time
    expires_at = models.IntegerField()
    # ...

    def to_token(self):
        return dict(
            access_token=self.access_token,
            token_type=self.token_type,
            refresh_token=self.refresh_token,
            expires_at=self.expires_at,
        )
