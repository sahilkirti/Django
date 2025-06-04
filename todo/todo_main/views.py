from django.shortcuts import render
from todos.models import Task
def home(request):
    tasks = Task.objects.filter(is_Completed = False).order_by('updated_at')
    completed_tasks = Task.objects.filter(is_Completed = True)
    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request, 'home.html', context)