from uuid import uuid4
from django import forms
from django.contrib.auth import get_user_model
from accounts.models import User
from trainingapps.tasks import send_activation_email


class SignUpForm(forms.ModelForm):
    password = forms.CharField(min_length=6)
    confirm_password = forms.CharField(min_length=6)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password',
            'confirm_password',
        )
        # ^ Reassign field widgets via forms, best practice.

    def clean(self):  # 1.Method validation
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['confirm_password']:
                raise forms.ValidationError('Passwords missmatch!')

        return cleaned_data

    def save(self, commit=True):  # 2.Method save
        instance: User = super().save(commit=False)
        instance.username = str(uuid4())
        instance.is_active = False
        # ^ if is_active == False, account denied login
        instance.set_password(self.cleaned_data['password'])
        # ^ Hashing password

        if commit:
            instance.save()
        send_activation_email.delay(username=self.instance.username, email_to=self.instance.email)

        return instance
