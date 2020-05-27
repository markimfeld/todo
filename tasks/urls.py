from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_list', views.new_list, name='new_list'),
    path('new_tag', views.new_tag, name='new_tag'),
    # path('new_task', views.new_task, name='new_task'),
    path('delete-list/<int:pk>', views.delete_list, name='delete_list'),
    path('delete-task/<int:list_pk>/<int:task_pk>', views.delete_task, name='delete_task')
]