from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Comments(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        'accounts.User', related_name='comments', on_delete=models.CASCADE)
    subject = models.ForeignKey(
        'tasks.Tasks', related_name='subject', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
