from django.views.generic import CreateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from accounts.forms import SignUpForm
from django.views.generic import UpdateView, TemplateView
from django.shortcuts import get_object_or_404
# Create your views here.


class SingUpView(CreateView):
    queryset = get_user_model()
    form_class = SignUpForm
    success_url = reverse_lazy("main")

    template_name = "singup.html"


class UserActivateView(RedirectView):
    pattern_name = None
    # ^ pattern_name = reverse_lazy/reverse(url)

    def get(self, request, *args, **kwargs):
        username = kwargs.pop("username")
        user = get_object_or_404(get_user_model(), username=username)

        if user.is_active:
            self.pattern_name = "account_is_activated"

        else:
            self.pattern_name = "activate_account"
            user.is_active = True
            user.save()

        response = super().get(request, *args, **kwargs)

        return response


class UserUpdateView(LoginRequiredMixin, UpdateView):
    queryset = get_user_model().objects.all()
    success_url = reverse_lazy("main")

    template_name = "my_profile.html"

    fields = (
        "first_name",
        "last_name",
    )  # ^ Creating fields in the model if the creation of the form is not required

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)

    #     return queryset
    # ^ Return isolated query

    def get_object(self, queryset=None):
        return self.request.user
    # ^ Return only needed query


class AccountConfirmView(TemplateView):
    extra_context = {
        "information": "Registration finished, account.",
    }

    template_name = "info.html"


class AccountPreviouslyConfirmView(TemplateView):
    extra_context = {
        "information": "Your account already activated!",
    }

    template_name = "info.html"
