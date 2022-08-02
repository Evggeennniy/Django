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
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy("rate_list")

    template_name = "create_rate.html"


class RateDetailsView(DeleteView):
    queryset = Rate.objects.all()

    template_name = "detail_rate.html"


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy("rate_list")

    template_name = "update_rate.html"


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy("rate_list")

    template_name = "delete_rate.html"


"""
CRUD WORKING WITH CONTACTUS
"""


class ContactUsCreateView(CreateView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    success_url = reverse_lazy("contactus_list")

    template_name = "create_contactus.html"


class ContactUsDetailsView(DeleteView):
    queryset = ContactUs.objects.all()

    template_name = "detail_contactus.html"


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    success_url = reverse_lazy("contactus_list")

    template_name = "update_contactus.html"


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    success_url = reverse_lazy("contactus_list")

    template_name = "delete_contactus.html"


"""
WORKING WITH SOURCE
"""


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "create_source.html"


class SourceDetailsView(DeleteView):
    queryset = Source.objects.all()

    template_name = "detail_source.html"


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "update_source.html"


class SourceDeleteView(DeleteView):
    queryset = SourceListView.queryset
    success_url = reverse_lazy("source_list")

    template_name = "delete_source.html"
