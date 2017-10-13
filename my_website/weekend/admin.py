from django.contrib import admin
from .models import Activity
from .forms import ActivityForm


class ActivityAdmin(admin.ModelAdmin):
    """Activity admin custom class."""

    form = ActivityForm
    list_display = [
        'name',
        'weather',
        'time',
        'fits_for',
        'category'
    ]
    list_filter = (
        ('name', admin.AllValuesFieldListFilter),
        ('weather', admin.ChoicesFieldListFilter),
        ('time', admin.ChoicesFieldListFilter),
        ('category', admin.ChoicesFieldListFilter),
    )
    readonly_fields = ['image_tag']


admin.site.register(Activity, ActivityAdmin)
