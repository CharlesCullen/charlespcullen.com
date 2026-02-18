from django.contrib import admin
from .models import Sponsor, HomepageSettings, Stat, FeaturedMedia


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')


@admin.register(HomepageSettings)
class HomepageSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if HomepageSettings.objects.exists():
            return False
        return True


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('value', 'label', 'order')
    ordering = ('order',)


@admin.register(FeaturedMedia)
class FeaturedMediaAdmin(admin.ModelAdmin):
    list_display = ('order', 'caption')
    ordering = ('order',)
