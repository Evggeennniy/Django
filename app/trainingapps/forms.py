from django import forms
from trainingapps.models import Rate, ContactUs, Source, ResponseLog

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
            "source"
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

        widgets = {
            "message": forms.Textarea()
        }  # ^ Reassign field widgets via forms, best practice.


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            "avatar",
            "source_url",
            "name"
        )


class ResponseLogForm(forms.ModelForm):
    class Meta:
        model = ResponseLog
        fields = (
            "response_time",
            "request_method",
            "query_params",
            "ip",
            "path",
        )
