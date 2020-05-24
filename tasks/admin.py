from django.contrib import admin
from .models import ListTask, Task, Tag


class ListTaskAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'completed', 'list_task')

class TagAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(ListTask, ListTaskAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)