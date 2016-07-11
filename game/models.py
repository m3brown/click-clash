from django.db import models
from django.conf import settings

class Counter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.count)
