from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from my_website.settings import MEDIA_URL
from my_website.settings import MEDIA_ROOT
from multipleselectionfield import MultipleSelectionField


CATEGORY_CHOICES = (
    ('sport', 'Sport'),
    ('movie', 'Movie'),
    ('concert', 'Concert'),
    ('museum', 'Museum'),
    ('food', 'Food'),
    ('market', 'Market'),
    ('party', 'Party'),
    ('short-trip', 'Short Trip'),
)

FITS_FOR_CHOICES = (
    ('alone', 'Alone'),
    ('couple', 'Couple'),
    ('family', 'Family'),
    ('group', 'Group'),
)

TIME_CHOICES = (
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
    ('full', 'Full day'),
)

WEATHER_CHOICES = (
    ('any', 'Any'),
    ('sunny', 'Sunny'),
    ('snow', 'Snow'),
    ('cold', 'Could'),
    ('warm', 'Warm'),
    ('rainy', 'Rainy'),
)


class Activity(models.Model):
    """Activity model."""
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    creator = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    reason = models.CharField(max_length=100)
    fits_for = MultipleSelectionField(
        max_length=200,
        choices=FITS_FOR_CHOICES,
    )
    time = models.CharField(
        max_length=20,
        choices=TIME_CHOICES,
        default='evening'
    )
    weather = models.CharField(
        max_length=20,
        choices=WEATHER_CHOICES,
        default='any',
    )
    image = models.ImageField(blank=True, upload_to='activity_images')
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='concert',
    )
    created_at = models.DateTimeField(default=timezone.now)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{MEDIA_URL}/{self.image}" width="150" height="150" />')
        else:
            return ''

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name
