from django.forms import ModelForm
from .models import Source, Stat


class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = '__all__'


class StatForm(ModelForm):
    class Meta:
        model = Stat
        fields = '__all__'
