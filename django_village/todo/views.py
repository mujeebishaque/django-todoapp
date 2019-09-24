from django.shortcuts import render, get_object_or_404, redirect
from todo.models import Todo
from django.http import HttpResponse

# Create your views here.

def index(request):

	if request.method == 'GET':
		todos = Todo.objects.all()
		return render(request, 'index.html', {'todos': todos} )

	if request.method == 'POST':
		todo = request.POST['todo']
		
		if not todo or len(todo) < 3:
			return "Invalid Todo"

		new_todo = Todo()
		new_todo.todo = todo
		new_todo.save()
		return redirect('index')

def mark_complete(request, todo_id):
	previous_todo = get_object_or_404(Todo, pk=todo_id)
	
	if previous_todo.is_complete:
    		previous_todo.is_complete = False
	else:
    		previous_todo.is_complete = True
	previous_todo.save()
	return redirect('index')

def delete(request, todo_id):
	delete_todo = get_object_or_404(Todo, pk=todo_id)
	delete_todo.delete()
	return redirect('index')

def update(request, todo_id):
	return render(request, 'update.html', {'todo_id': todo_id})
