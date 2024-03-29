from django.shortcuts import render
from django.views import generic as views
from MenTEL_website_softuni_django_exam.common.profile_helpers import get_profile
from django.urls import reverse_lazy


class IndexView(views.TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_profile()
        return context

class MobileplansView(views.TemplateView):
    template_name = 'web/index-plans.html'
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
class HistoryView(views.TemplateView):
    template_name = 'web/index-history.html'
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
class ContactsView(views.TemplateView):
    template_name = 'web/index-contacts.html'
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()

