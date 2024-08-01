from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
            'desc',
            'app',
            'length',
            'width',
            'height',
            'color',
            'occupants',
            'window_num',
            'window_size',
            'window_orientation',
            'lamp_specs',
            'aircond_type'
        ]
        widgets = {
            'color': forms.ColorInput(attrs={'title': 'Choose your color'}),
            'length': forms.NumberInput(attrs={'min': 0}),
            'width': forms.NumberInput(attrs={'min': 0}),
            'height': forms.NumberInput(attrs={'min': 0}),
            'window_size': forms.NumberInput(attrs={'min': 0}),
            'window_num': forms.NumberInput(attrs={'min': 0}),
            'occupants': forms.NumberInput(attrs={'min': 0}),
        }

    # You can add custom validation if needed
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here if needed
        return cleaned_data
