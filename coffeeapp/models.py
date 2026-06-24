from django.db import models
from django.utils import timezone
# from location_field.models.spatial import LocationField
from django_countries.fields import CountryField

from datetime import date

ROAST_LEVEL_CHOICES = (
    ('dark', 'Dark'),
    ('medium', 'Medium'),
    ('light', 'Light'),
    ('ultra-light', 'Ultra-light'),
)

# Create your models here.

class Roaster(models.Model):
    name = models.CharField(max_length=200)
    # roaster_location = LocationField(zoom=7, default=Point(1.0, 1.0))

    def __str__(self):
        return self.name

class TastingNote(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField("date added", default=timezone.now)
    roast_date = models.DateField("roast date", default=date.today)
    roaster = models.ForeignKey(Roaster, on_delete=models.CASCADE)
    origin = CountryField()
    tasting_notes = models.ManyToManyField(TastingNote)
    roast_level = models.CharField(max_length=11, choices=ROAST_LEVEL_CHOICES, default='medium')

    def __str__(self):
        return self.name
