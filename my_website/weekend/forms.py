from django import forms
from .models import Activity
from .models import FITS_FOR_CHOICES


class ActivityForm(forms.ModelForm):
    """Customized form for model Activity."""
    fits_for = forms.MultipleChoiceField(
        choices=FITS_FOR_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Activity
        fields = [
            'name',
            'description',
            'reason',
            'time',
            'weather',
            'fits_for',
            'category',
            'creator',
            'image'
        ]
