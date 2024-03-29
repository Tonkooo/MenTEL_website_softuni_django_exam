from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from django.views import generic as views
from MenTEL_website_softuni_django_exam.profiles.models import Profile
from MenTEL_website_softuni_django_exam.common.profile_helpers import get_profile

class RegisterView(views.CreateView):
    model = Profile
    template_name = 'profile/profile-login-form.html'
    fields = ["username", "email", "age", "password"]
    success_url = reverse_lazy('catalogue')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_profile()
        return context
