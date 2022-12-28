from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f'{self.id} {self.title}'
