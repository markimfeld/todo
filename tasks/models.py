from django.db import models

# Create your models here.
class ListTask(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=30)
    last_edited_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(null=False)
    list_task = models.ForeignKey(ListTask, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name
