from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    listaTareas = Task.objects.all()
    return render(request, "list_tasks.html", {"tasks": listaTareas})


def create_task(request):
    nuevoTitulo = request.POST["title"]
    nuevaDescripcion= request.POST["description"]
    
    if nuevoTitulo == "" or nuevaDescripcion == "":
        tareas = Task.objects.all()
        return render(
            request, "list_tasks.html", {"tasks": tareas, "error": "Debes ingresar título y descripción"}
        )
    crearTarea = Task(title=nuevoTitulo, description=nuevaDescripcion)
    crearTarea.save()
    return redirect("/tasks/")


def delete_task(request, task_id):
    borrarTarea = Task.objects.get(id=task_id)
    borrarTarea.delete()
    return redirect("/tasks/")
