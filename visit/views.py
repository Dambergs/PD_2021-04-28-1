from django.shortcuts import render
from django.views.generic import ListView, View, FormView, DetailView
from visit.models import Visit, Room
from visit.forms import VisitForm


class VisitListView(ListView):

    model = Visit
    template_name = 'visit_list.html'


class VisitDetailView(DetailView):

    model = Visit
    template_name = 'visit_detail.html'


class AddVisitView(FormView):

    form_class = VisitForm
    template_name = 'add_visit.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response


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



