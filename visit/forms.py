from django import forms
from visit.models import Visit
#from django_visits.visit.models import Visit

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = [
            'name',
            'date',
            'reason',
            'room',
        ]
