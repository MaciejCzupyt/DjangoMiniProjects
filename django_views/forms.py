from django import forms
from .models import ExampleModel


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        # either "fields" or "exclude"
        fields = "__all__"
