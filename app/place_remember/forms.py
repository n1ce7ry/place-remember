from django import forms
from .models import Memory


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['name', 'description', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'latitude': forms.HiddenInput(attrs={'required': True}),
            'longitude': forms.HiddenInput(attrs={'required': True}),
        }
