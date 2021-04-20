from django.shortcuts import render
from visit.models import Visit, Room


def index(request):

    visits = Visit.objects.all()

    context = {
        'visits': visits,
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_visit(request):

    if request.method == 'POST':

        room_id = int(request.POST['room_id'])
        room = Room.objects.get(id=room_id)

        visit = Visit(
            name=request.POST['name'],
            date=request.POST['date'],
            reason=request.POST['reason'],
            room=room,
        )

        visit.save()

        context = {
            'visit': visit,
        }

        return render(
            template_name='visit.html',
            request=request,
            context=context,
        )

    return render(
        template_name='form.html',
        request=request,
    )
