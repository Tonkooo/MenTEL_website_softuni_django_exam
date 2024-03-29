from MenTEL_website_softuni_django_exam.profiles.models import Profile
def get_profile():
    return Profile.objects.first()