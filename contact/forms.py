from django import forms

from .models import massage


class masseg_form (forms.ModelForm):
    class Meta:
        model = massage
        fields = ('name', 'emale', 'subject', 'text')
