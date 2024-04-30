from django.shortcuts import render ,redirect
from todo_app.forms import TodoForm
from todo_app.models import TodoModel
# Create your views here.
def home (request):
    return render(request,'add_task.html')

def add_task(request):
    if request.method =='POST':
        todo = TodoForm(request.POST)
        if todo.is_valid():
            print(todo.cleaned_data)
            todo.save()
            return redirect('taskList')
            
    else :
            todo=TodoForm()
    return render(request,'add_task.html',{'form':todo})

def task_list(request):
    todo = TodoModel.objects.all()

    return render(request,'task_list.html', {'data':todo})

def edit_list(request,id):
    todo = TodoModel.objects.get(pk = id )
    form = TodoForm(instance = todo)
    if request.method =='POST':
        todo = TodoForm(request.POST,instance = todo)
        if todo.is_valid():
            todo.save()
            return redirect('taskList')
    return render(request,'add_task.html',{'form':form})

def delete_list(request,id):
    todo = TodoModel.objects.get(pk = id ).delete()
    return redirect('taskList')