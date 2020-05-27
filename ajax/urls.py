from django.urls import path

from . import views

app_name = 'ajax'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete, name='delete_task')
]