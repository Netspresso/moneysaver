from django.shortcuts import render, get_object_or_404, redirect
from .models import Cel
from django.contrib.auth.decorators import login_required
from .forms import AimsForm
from django.db.models import Sum
from datetime import datetime
import math


def all_aims(request):
    ''' Takes all Cel objects from db and generate dynamic template using this objects '''
    aims = Cel.objects.all()
    # Here I calculate the sum cost of all aims and Here I create functionality that calculate monthly savings
    suma = 0
    weekly_sum = 0
    now = datetime.now().date()

    for aim in aims:
        suma += aim.kwota
        delta = now - aim.data
        weekly_sum += aim.kwota / delta.days * 7

    weekly_sum = math.ceil(abs(weekly_sum))

    return render(request, 'cele.html', {
        'cele': aims,
        'suma': suma,
        'weekly_sum': weekly_sum
    })


@login_required
def new_aim(request):
    ''' Displays form that allow legged user to add new aim '''
    aims_form = AimsForm(request.POST or None, request.FILES or None)

    if all(aims_form.is_valid()):
        aim = aims_form.save(commit=False)
        aim.save()
        return redirect(all_aims)

    return render(request, 'aims_form.html', {'form': aims_form, 'new': True})


@login_required
def edit_aim(request, id):
    ''' Displays edit form that allow logged user to edit his aims '''
    movie = get_object_or_404(Cel, pk=id)
    aims_form = AimsForm(request.POST or None,
                         request.FILES or None,
                         instance=movie)
    if aims_form.is_valid():
        movie = aims_form.save(commit=False)
        movie.save()
        return redirect(all_aims)
    return render(request, 'aims_form.html', {'form': aims_form, 'new': False})


@login_required
def delete_aim(request, id):
    ''' Display submit screen and allow logged user to delete his aims one by one '''
    aim = get_object_or_404(Cel, pk=id)

    if request.method == 'POST':
        aim.delete()
        return redirect(all_aims)

    return render(request, 'submit.html', {'cel': aim})
