from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('id', 'done')
    context = {
        'tasks': tasks
    }
    return render(request, 'todos/index.html', context)


@require_http_methods(['GET', 'POST'])
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title', '')
        task.save()

        context = {
            'task': task
        }
        return render(request, 'todos/partials/task.html', context)

    context = {
        'task': task
    }
    return render(request, 'todos/partials/edit.html', context)


@require_http_methods(['POST'])
def add_task(request):
    task = None
    title = request.POST.get('title', '')

    if title:
        task = Task.objects.create(title=title)

    context = {
        'task': task
    }

    return render(request, 'todos/partials/task.html', context)


@require_http_methods(['PUT'])
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = True
    task.save()

    context = {
        'task': task
    }

    return render(request, 'todos/partials/task.html', context)


@require_http_methods(['DELETE'])
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()

    return HttpResponse()
