from .models import HomepageSettings

def global_homepage(request):
    homepage = HomepageSettings.objects.first()
    return {
        'homepage': homepage
    }
