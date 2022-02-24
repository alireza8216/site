
from django import forms
from django.utils import timezone
from .models import massage


class masseg_form (forms.ModelForm):
    class Meta:
        model = massage
        fields = ['subject','emale','text','profile']
    
