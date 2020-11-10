from django.shortcuts import render, HttpResponse,redirect
from .models import Shows
from the_app import app_filters
from django.contrib import messages
from datetime import datetime

def shows(request):
    context = {
    "shows" : Shows.objects.all(),
    }
    return render(request, 'shows.html', context)

def add_show_temp(request):
    return render(request, 'add_show.html')

def add_show(request):
    if request.method == 'POST':
        response_from_models = Shows.objects.validate(request.POST)

        if len(response_from_models) < 1:
            new_show = Shows(title=request.POST['the_title'], network=request.POST['network'], release_date=request.POST['date'] , desc=request.POST['desc'])
            new_show.save()
            id = new_show.id
            return redirect(view, show_id = int(id) )
        
        else:
            # send E msgs to C
            for err in response_from_models:
                messages.error(request, err)

    return redirect(add_show_temp)
            

def view(request, show_id):
    context = {
    "show" : Shows.objects.get(id=show_id),
    }
    return render(request, 'view_show.html', context)

def edit(request, show_id):
    context = {
    "show" : Shows.objects.get(id=show_id),
    }
    return render(request, 'edit_show.html', context)


def delete(request, show_id):
    show = Shows.objects.get(id=show_id)
    show.delete()
    return redirect(shows)

def update(request, show_id):
    if request.method == 'POST':
        response_from_models = Shows.objects.validate(request.POST)

        if len(response_from_models) < 1:
            Shows.objects.filter(id=show_id).update(
                title=request.POST['the_title'], 
                network=request.POST['network'], 
                release_date=request.POST['date'], 
                desc=request.POST['desc'],
                updated_at=datetime.now()
            )
            return redirect(view, show_id=request.POST['id'])
        
        else:
            # send E msgs to C
            for err in response_from_models:
                messages.error(request, err)

    return redirect(edit, show_id=request.POST['id'])