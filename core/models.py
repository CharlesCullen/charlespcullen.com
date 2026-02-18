from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    logo = models.ImageField(upload_to='sponsors/', blank=True, null=True)

    def __str__(self):
        return self.name


class HomepageSettings(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.CharField(max_length=300)
    hero_image = models.ImageField(upload_to='hero/')

    about_text = models.TextField()
    about_image = models.ImageField(upload_to='about/')

    site_logo = models.ImageField(upload_to='branding/', blank=True, null=True)

    def __str__(self):
        return "Homepage Settings"


class Stat(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.value} {self.label}"


class FeaturedMedia(models.Model):
    image = models.ImageField(upload_to='featured/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Featured Media {self.order}"
