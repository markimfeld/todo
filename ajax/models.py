from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=64)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name