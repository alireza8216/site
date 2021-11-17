from django import forms
from .models import coment


class comment_form (forms.ModelForm):
    class Meta :
        model = coment
        fields = ('name','email','website','text')