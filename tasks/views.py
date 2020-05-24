from django.shortcuts import render
from django.http import (
    HttpResponse, 
    HttpResponseRedirect,
    JsonResponse
)
from django.urls import reverse
from django.forms.models import model_to_dict



from tasks.models import (
    ListTask, 
    Task, 
    Tag
)
from .forms import (
    NewListForm,
    NewTaskForm,
    NewTagForm
)

def is_valid_queryparam(param):
    return param != '' and param is not None

def index(request):
    tag = request.GET.get("tag")

    tags = Tag.objects.all()
    lists = ListTask.objects.all()

    if is_valid_queryparam(tag):
        filter_tag = tags.get(name=tag)
        lists = lists.filter(tags=filter_tag).all()

    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/index.html', {
                'form': NewTaskForm()
            })


    return render(request, 'tasks/index.html', {
        'form': NewTaskForm(),
        'lists': lists,
        'tags': tags
    })

def new_list(request):

    tags = Tag.objects.all()

    if request.method == 'POST':
        form = NewListForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/new_list.html', {
                'form': NewListForm()
            })

    return render(request, 'tasks/new_list.html', {
        'form': NewListForm(),
        'tags': tags
    })

def new_tag(request):

    if request.method == 'POST':
        form = NewTagForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('tasks:new_list'))
        else:
            return render(request, 'tasks/new_tag.html', {
                'form': NewTagForm()
            })
    return render(request, 'tasks/new_tag.html', {
        'form': NewTagForm()
    })

# def new_task(request):
#     lists = ListTask.objects.all()

#     if request.method == 'POST':
#         form = NewTaskForm(request.POST)

#         if form.is_valid():
#             form = form.save()
#             return HttpResponseRedirect(reverse('tasks:index'))
#         else:
#             return render(request, 'tasks/index.html', {
#                 'form': NewTaskForm()
#             })

#     return render(request, 'tasks/index.html', {
#         'form': NewTaskForm(),
#         'lists': lists
#     })

def delete_list(request, pk):

    lista = ListTask.objects.get(pk=pk)

    if lista is not None:
        lista.delete()
    
    return HttpResponseRedirect(reverse('tasks:index'))