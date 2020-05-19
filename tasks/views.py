from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

from tasks.models import ListTask, Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Check email, do exercise, etc...'
                }
            ),
            'completed': forms.CheckboxInput(
                attrs = {
                    'class': 'form-check-input',
                }
            ),
            'list_task': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }

# Create your views here.
def index(request):
    lists = ListTask.objects.all()
    list_task = ListTask.objects.get(pk=1)
    # tasks = Task.objects.filter(list_task=list_task).all()
    tasks = Task.objects.all()

    listas = dict()

    for l in lists:
        print(l)


    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'list_task': list_task,
        'lists': lists
    })

def add(request):
    lists = ListTask.objects.all()

    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {
                'form': NewTaskForm()
            })

    return render(request, 'tasks/add.html', {
        'form': NewTaskForm(),
        'lists': lists
    })