from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    form = TaskForm()

    if request.method == "POST":
        #Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/Todo/index/')
    task_form = Task.objects.all()        
    return render(request,'todoapp/index.html',{'task_form': form})


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/Todo/index/')

    return render(request, 'todoapp/update.html', {'task_edit_form': form})   


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/Todo/index/')      