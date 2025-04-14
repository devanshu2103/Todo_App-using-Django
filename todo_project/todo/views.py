from django.shortcuts import redirect,render, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})



def task_create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'todo/task_form.html')




def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'todo/task_form.html', {'task': task})

from django.shortcuts import get_object_or_404, redirect
from .models import Task




def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')
