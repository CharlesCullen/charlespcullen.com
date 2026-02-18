from .models import Sponsor, HomepageSettings, Stat, FeaturedMedia

from django.shortcuts import render

def home(request):
    sponsors = Sponsor.objects.all()
    homepage = HomepageSettings.objects.first()
    stats = Stat.objects.all()
    featured_media = FeaturedMedia.objects.all()

    return render(request, 'pages/home.html', {
        'sponsors': sponsors,
        'homepage': homepage,
        'stats': stats,
        'featured_media': featured_media
    })

def about(request):
    return render(request, "pages/about.html")

def partners(request):
    sponsors = Sponsor.objects.all()
    return render(request, "pages/partners.html", {"sponsors": sponsors})
