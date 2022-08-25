from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
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
    template_name = "index.html"


class RateListView(LoginRequiredMixin, ListView):
    queryset = Rate.objects.all().select_related("source")
    form_class = RateForm
    success_url = reverse_lazy("rate_list")

    template_name = "rate_list.html"


class ContactUsListView(LoginRequiredMixin, ListView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    success_url = reverse_lazy("contactus_list")

    template_name = "contactus_list.html"


class SourceListView(LoginRequiredMixin, ListView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy("source_list")

    template_name = "source_list.html"


class ResponseLogListView(LoginRequiredMixin, ListView):
    queryset = ResponseLog.objects.all()
    form_class = ResponseLogForm
    success_url = reverse_lazy("response_list")

    template_name = "response_list.html"


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


class RateUpdateView(OnlySuperUser, UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy("rate_list")

    template_name = "update_rate.html"


class RateDeleteView(OnlySuperUser, DeleteView):
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

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields["message"].widget = forms.Textarea()

    #     return form
    # ^ Reassign field widgets directly via views(Not best practice)

    def form_valid(self, form):
        response = super().form_valid(form)

        subject = "Subject Django Project"
        message = f"""
        Subject : {self.object.subject}
        Message : {self.object.message}
        """
        email_to = self.object.email_to

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email_to],
            fail_silently=False,
        )  # ^ Sending messages

        return response


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
