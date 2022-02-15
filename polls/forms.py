from django import forms

from .models import Sondage

class PollForm(forms.ModelForm):
    class Meta:
        model = Sondage
        fields = [
            'question',
            'res_1',
            'res_2',
            'res_3',
        ]