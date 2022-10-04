from django.db import models

# Create your models here.


class Snippet(models.Model):
    owner = models.ForeignKey(
        'accounts.User', related_name='snippets', on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()

    def __str__(self):
        return self.title
