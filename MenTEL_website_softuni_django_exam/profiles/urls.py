from django.urls import path
from MenTEL_website_softuni_django_exam.profiles.views import RegisterView

urlpatterns = [
    path('create/', RegisterView.as_view(), name='register view'),
]