from django import forms
from trainingapps.models import Source


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            "source_url",
            "name"
        )
