from django.shortcuts import render
from django.views.generic import ListView, View
from visit.models import Visit, Room


class VisitListView(ListView):

    model = Visit
    template_name = 'visit_list.html'


class AddVisitView(View):

    def get(self, request):

        return render(
            template_name='form.html',
            request=request,
        )

    def post(self, request):

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


class FilterByDate(View):

    def get(self, request):

        return render(
            template_name='filter_by_date.html',
            request=request,
        )

    def post(self, request):

        date = request.POST['date']
        visits = Visit.objects.filter(date=date)

        context = {
            'visits': visits,
        }

        return render(
            template_name='visit_list.html',
            request=request,
            context=context,
        )


class FilterByRoom(View):

    def get(self, request):

        return render(
            template_name='filter_by_room.html',
            request=request,
        )

    def post(self, request):

        room_id = request.POST['room_id']
        visits = Visit.objects.filter(room__id=room_id)

        context = {
            'visits': visits,
        }

        return render(
            template_name='visit_list.html',
            request=request,
            context=context,
        )



