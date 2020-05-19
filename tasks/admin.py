from django.contrib import admin
from .models import ListTask, Task


class ListTaskAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(ListTask, ListTaskAdmin)
admin.site.register(Task, TaskAdmin)