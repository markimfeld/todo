from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('marcos', views.marcos, name='marcos'),
    path('<str:name>', views.greeting, name='greeting')
]