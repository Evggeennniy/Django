from django import forms
from trainingapps.models import Rate, ContactUs, Source

"""
In Django, we use Django models to design our database tables and their fields.
If we need to add data about the model itself, we use the Meta class.
"""


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            "ccy",
            "base_ccy",
            "buy",
            "sell",
        )  # ^ Forms for data manipulation, creation, modification, deletion and so on.


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            "email_from",
            "email_to",
            "subject",
            "message",
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            "source_url",
            "name"
        )
