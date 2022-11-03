from django.urls import reverse_lazy
from trainingapps.tasks import sending_mail
# ^ Dependencies
from trainingapps.models import Rate, ContactUs, Source, ResponseLog
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from trainingapps.forms import RateForm, SourceForm, ContactUsForm, ResponseLogForm
# ^ A work with models and form
from django.contrib.auth.mixins import LoginRequiredMixin
# ^ The module connects to classes,
# access to the capabilities of the class to which the module was connected
# will depend on the presence of the user's sessionid key
from django.contrib.auth.mixins import UserPassesTestMixin
# ^ Users pass
from django_filters.views import FilterView
# ^ Used filter views for filter in listview
from trainingapps.filters import RateFilter
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
"""
USERS PASS
"""


class OnlySuperUser(UserPassesTestMixin):
    permission_denied_message = 'Trying to bypass the system !'

    def test_func(self):
        return self.request.user.is_superuser
    # ^ if tests be false, return perm. denided


"""
CRUD WORKING WITH GENERAL
"""


class IndexView(TemplateView):
    template_name = "currency/index.html"


@method_decorator(cache_page(10), name='dispatch')
class RateListView(LoginRequiredMixin, FilterView):
    queryset = Rate.objects.get_queryset().order_by('id')
    queryset = queryset.select_related("source")
    # ^ .select_related() = JOIN table
    form_class = RateForm
    success_url = reverse_lazy("rate_list")

    page_size_options = [10, 15, 20]
    filterset_class = RateFilter

    template_name = "currency/rate_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        filter_params = self.request.GET.copy()

        if self.page_kwarg in filter_params:
            del filter_params[self.page_kwarg]
        # ^ Delete old filter params

        context['filter_params'] = filter_params.urlencode()
        context['page_size'] = self.get_paginate_by()
        context['page_size_options'] = self.page_size_options
        # ^ Put to context a needed params

        return context
    # ^ Fix url request get params

    def get_paginate_by(self, queryset=None):
        """
        Get page size from params or get default
        """
        if 'page_size' in self.request.GET:
            paginate_by = int(self.request.GET['page_size'])
        else:
            paginate_by = 15

        return paginate_by
    # ^ Set objects in page


@method_decorator(cache_page(10), name='dispatch')
class ContactUsListView(ListView):
    queryset = ContactUs.objects.get_queryset().order_by('id')
    form_class = ContactUsForm
    success_url = reverse_lazy("contactus_list")

    template_name = "currency/contactus_list.html"


@method_decorator(cache_page(10), name='dispatch')
class SourceListView(LoginRequiredMixin, ListView):
    queryset = Source.objects.get_queryset().order_by('id')
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "currency/source_list.html"


@method_decorator(cache_page(30), name='dispatch')
class ResponseLogListView(LoginRequiredMixin, ListView):
    queryset = ResponseLog.objects.get_queryset().order_by('id')
    form_class = ResponseLogForm
    success_url = reverse_lazy("response_list")

    template_name = "currency/response_list.html"


"""
CRUD WORKING WITH RATE
"""


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy("rate_list")

    template_name = "currency/create_rate.html"


class RateDetailsView(DeleteView):
    queryset = Rate.objects.all()

    template_name = "currency/detail_rate.html"


class RateUpdateView(OnlySuperUser, UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy("rate_list")

    template_name = "currency/update_rate.html"


class RateDeleteView(OnlySuperUser, DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy("rate_list")

    template_name = "currency/delete_rate.html"


"""
CRUD WORKING WITH CONTACTUS
"""


class ContactUsCreateView(CreateView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    success_url = reverse_lazy("contactus_list")

    template_name = "currency/create_contactus.html"

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields["message"].widget = forms.Textarea()

    #     return form
    # ^ Reassign field widgets directly via views(Not best practice)

    def form_valid(self, form):
        response = super().form_valid(form)

        sending_mail.delay(self.object.subject, self.object.email_from, self.object.email_to)
        # ^ if form is valid use a next do

        return response


class ContactUsDetailsView(DeleteView):
    queryset = ContactUs.objects.all()

    template_name = "currency/detail_contactus.html"


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    success_url = reverse_lazy("contactus_list")

    template_name = "currency/update_contactus.html"


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    success_url = reverse_lazy("contactus_list")

    template_name = "currency/delete_contactus.html"


"""
WORKING WITH SOURCE
"""


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "currency/create_source.html"


class SourceDetailsView(DeleteView):
    queryset = Source.objects.all()

    template_name = "currency/detail_source.html"


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "currency/update_source.html"


class SourceDeleteView(DeleteView):
    queryset = SourceListView.queryset
    success_url = reverse_lazy("source_list")

    template_name = "currency/delete_source.html"
