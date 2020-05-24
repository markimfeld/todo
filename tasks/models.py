from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class ListTask(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
    last_edited_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    list_task = models.ForeignKey(ListTask, on_delete=models.CASCADE, default=0, related_name="tasks")

    def __str__(self):
        return self.name
