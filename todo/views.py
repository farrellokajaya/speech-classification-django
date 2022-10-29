from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages

from .models import Task
from .forms import TaskForm


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'todo/index.html', context)

def detail_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }
    except Task.DoesNotExist:
        raise Http404("Task tidak ditemukan.")
    return render(request, 'todo/detail.html', context)

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = TaskForm(request.POST)
            new_task.save()
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('todo:index')
    else:
        form = TaskForm()
    return render(request, 'todo/form.html', {'form': form})

def update_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task tidak ditemukan.")
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses Mengubah Task.')
            return redirect('todo:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/form.html', {'form': form})

def delete_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        messages.success(request, 'Sukses Menghapus Task.')
        return redirect('todo:index')
    except Task.DoesNotExist:
        raise Http404("Task tidak ditemukan.")

