from MenTEL_website_softuni_django_exam.web.views import IndexView, MobileplansView, HistoryView, ContactsView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mobileplans/', MobileplansView.as_view(), name='mobileplans'),
    path('history/', HistoryView.as_view(), name='history'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
