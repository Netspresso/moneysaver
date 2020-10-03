from django.forms import ModelForm
from .models import Cel


class AimsForm(ModelForm):
    class Meta:
        model = Cel
        fields = [
            'cel',
            'data',
            'kwota',
        ]
