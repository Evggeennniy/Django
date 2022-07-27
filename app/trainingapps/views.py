from django.urls import reverse_lazy
from trainingapps.models import ContactUs, Rate, Source
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from trainingapps.forms import SourceForm


"""
WORKING WITH PAGES
"""


class IndexView(TemplateView):
    template_name = "index.html"


class RateListView(ListView):
    queryset = Rate.objects.all()  # Selected db

    template_name = "rate_list.html"


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()  # Selected db

    template_name = "contactus_list.html"


class SourceListView(ListView):
    queryset = Source.objects.all()  # Selected db

    template_name = "source_list.html"


"""
WORKING WITH SOURCE
"""


class SourceCreateView(CreateView):
    queryset = SourceListView.queryset
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "create_source.html"


class SourceDetailsView(DeleteView):
    queryset = SourceListView.queryset

    template_name = "detail_source.html"


class SourceUpdateView(UpdateView):
    queryset = SourceListView.queryset
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "update_source.html"


class SourceDeleteView(DeleteView):
    queryset = SourceListView.queryset
    extra_context = {"database": queryset}
    success_url = reverse_lazy("source_list")

    template_name = "delete_source.html"
