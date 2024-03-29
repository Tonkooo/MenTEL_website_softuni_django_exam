from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MenTEL_website_softuni_django_exam.web.urls')),
    path('devices/', include('MenTEL_website_softuni_django_exam.devices.urls')),
    path('plans/', include('MenTEL_website_softuni_django_exam.plans.urls')),
    path('profile/', include('MenTEL_website_softuni_django_exam.profiles.urls')),
]