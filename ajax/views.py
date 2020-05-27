from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from django.urls import reverse

from .models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Add new task..'
                }
            )
        }


def index(request):

    tasks = Task.objects.all()

    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            new_task = form.save()

            if new_task is not None:
                return JsonResponse({'task': model_to_dict(new_task)}, status=200)
        else:
            return render(request, 'ajax/index.html', {
                'form': NewTaskForm(),
                'tasks': tasks
            })

    return render(request, 'ajax/index.html', {
        'form': NewTaskForm(),
        'tasks': tasks
    })


def delete(request, pk):

    task = Task.objects.get(pk=pk)

    if task is not None:
        task.delete()
    
    return HttpResponseRedirect(reverse('ajax:index'))