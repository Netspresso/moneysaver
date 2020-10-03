from django.shortcuts import render, get_object_or_404, redirect
from .models import Cel
from django.contrib.auth.decorators import login_required
from .forms import AimsForm


def all_aims(request):
    aims = Cel.objects.all()
    return render(request, 'cele.html', {'cele': aims})


@login_required
def new_aim(request):
    aims_form = AimsForm(request.POST or None, request.FILES or None)

    if all(aims_form.is_valid()):
        aim = aims_form.save(commit=False)
        aim.save()
        return redirect(all_aims)

    return render(request, 'aims_form.html', {'form': aims_form, 'new': True})


@login_required
def edit_aim(request, id):
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
    aim = get_object_or_404(Cel, pk=id)

    if request.method == 'POST':
        aim.delete()
        return redirect(all_aims)

    return render(request, 'submit.html', {'cel': aim})
