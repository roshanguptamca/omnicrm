from django.db import models
from uuid import uuid4


# Create your models here.
class Session(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    actor = models.CharField(max_length=100)
    uuid = models.UUIDField(unique=True, default=uuid4)

    def __str__(self):
        return str(self.uuid)


class Task(models.Model):
    TASK_CHOICES = [
        ('CASE', 'Case'),
    ]

    task_type = models.CharField(choices=TASK_CHOICES, max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    krn = models.CharField(null=True, max_length=16)

    def __str__(self):
        return 'Task (ID: {}, Type: {})'.format(self.pk, self.task_type)


class Log(models.Model):
    LOG_CHOICES = [
        ('NOTE', 'Note'),
        ('TASK', 'Task')
    ]

    log_type = models.CharField(choices=LOG_CHOICES, max_length=20)
    reference_id = models.CharField(null=True, max_length=50)
    description = models.TextField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
