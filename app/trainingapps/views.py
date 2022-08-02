from django.urls import reverse_lazy
from trainingapps.models import ContactUs, Rate, Source
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from trainingapps.forms import RateForm, SourceForm, ContactUsForm


"""
CRUD WORKING WITH GENERAL
"""


class IndexView(TemplateView):
    template_name = "index.html"


class RateListView(ListView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy("rate_list")

    template_name = "rate_list.html"


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    success_url = reverse_lazy("contactus_list")

    template_name = "contactus_list.html"


class SourceListView(ListView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "source_list.html"


"""
CRUD WORKING WITH RATE
"""


class RateCreateView(CreateView):
    queryset = RateListView.queryset
    form_class = RateListView.form_class
    success_url = RateListView.success_url

    template_name = "create_source.html"


class RateDetailsView(DeleteView):
    queryset = RateListView.queryset

    template_name = "detail_rate.html"


class RateUpdateView(UpdateView):
    queryset = RateListView.queryset
    form_class = RateListView.form_class
    success_url = RateListView.success_url

    template_name = "update_rate.html"


class RateDeleteView(DeleteView):
    queryset = RateListView.queryset
    success_url = RateListView.success_url

    template_name = "delete_rate.html"


"""
CRUD WORKING WITH CONTACTUS
"""


class ContactUsCreateView(CreateView):
    queryset = ContactUsListView.queryset
    form_class = ContactUsListView.form_class
    success_url = ContactUsListView.success_url

    template_name = "create_contactus.html"


class ContactUsDetailsView(DeleteView):
    queryset = ContactUsListView.queryset

    template_name = "detail_contactus.html"


class ContactUsUpdateView(UpdateView):
    queryset = ContactUsListView.queryset
    form_class = ContactUsListView.form_class
    success_url = ContactUsListView.success_url

    template_name = "update_contactus.html"


class ContactUsDeleteView(DeleteView):
    queryset = ContactUsListView.queryset
    success_url = ContactUsListView.success_url

    template_name = "delete_contactus.html"


"""
WORKING WITH SOURCE
"""


class SourceCreateView(CreateView):
    queryset = SourceListView.queryset
    form_class = SourceListView.form_class
    success_url = SourceListView.success_url

    template_name = "create_source.html"


class SourceDetailsView(DeleteView):
    queryset = SourceListView.queryset

    template_name = "detail_source.html"


class SourceUpdateView(UpdateView):
    queryset = SourceListView.queryset
    form_class = SourceListView.form_class
    success_url = SourceListView.success_url

    template_name = "update_source.html"


class SourceDeleteView(DeleteView):
    queryset = SourceListView.queryset
    success_url = SourceListView.success_url

    template_name = "delete_source.html"
