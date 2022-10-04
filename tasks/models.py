from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Tasks(models.Model):
    # class StatusChoice(models.TextChoices):
    #     PENDING = 'PEN', _('Pending')
    #     CANCELLED = 'CAN', _('Canceled'),
    #     COMPLETED = 'COM', _('Completed')

    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    # status = models.CharField(
    #     max_length=9, choices=StatusChoice.choices, default=StatusChoice.PENDING)
    author = models.ForeignKey(
        'accounts.User', related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_title(self):
        return self.title + " status: " + self.status
